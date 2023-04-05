""" Basic date and time concepts: relative date, date range, offset, business
    centre etc.
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case4, the example reflects the frequency data type from
# base-datetime-type.rosetta
from __future__ import annotations
from typing import List, Optional
from datetime import date
from pydantic import BaseModel, Field, validator, root_validator
from cdm import check_one_of_constraint
from base_datetime_enum import (PeriodExtendedEnum, BusinessCenterEnum,
                                 BusinessDayConventionEnum)

__all__ = [
    'BusinessCenters', 'BusinessDayAdjustments', 'AdjustableDates', 'Frequency'
]


class BusinessCenters(BaseModel):
    """ A class for specifying the business day calendar location used in
        determining whether a day is a business day or not, either by specifying
        this business center by reference to an enumerated list that is
        maintained by the FpML standard, or by reference to such specification
        when it exists elsewhere as part of the instance document. This class
        corresponds to the FpML BusinessCentersOrReference.model.
    """

    businessCenter: Optional[List[BusinessCenterEnum]] = Field(
        None,
        description='A code identifying one or several business day calendar '
                    'location(s). The set of business day calendar locations '
                    'are specified by the business day calendar location '
                    'enumeration which is maintained by the FpML standard.'
    )
    """ (0..*) A code identifying one or several business day calendar
        location(s). The set of business day calendar locations are specified by
        the business day calendar location enumeration which is maintained by
        the FpML standard.
    """
    businessCentersReference: Optional[BusinessCenters] = Field(
        None,
        description='A reference to a financial business center location '
                    'specified elsewhere in the instance document.'
    )
    """ (0..1) A reference to a financial business center location specified
        elsewhere in the instance document.
    """

    @root_validator
    @classmethod
    def condition_0_BusinessCentersChoice(cls, values):
        """ Choice rule to represent an FpML choice construct. """
        return check_one_of_constraint(values, 'businessCenter',
                                       'businessCentersReference')


class BusinessDayAdjustments(BaseModel):
    """ A class defining the business day convention and financial business
        centers used for adjusting any relevant date if it would otherwise fall
        on a day that is not a business day in the specified business center.
    """

    businessDayConvention: BusinessDayConventionEnum = Field(
        ...,
        description='The convention for adjusting a date if it would otherwise '
                    'fall on a day that is not a business day.'
    )
    """ (1..1) The convention for adjusting a date if it would otherwise fall
        on a day that is not a business day.
    """
    businessCenters: Optional[BusinessCenters] = Field(
        None,
        description='The business center(s), specified either explicitly or by '
                    'reference to those specified somewhere else in the '
                    'instance document.'
    )
    """ (0..1) The business center(s), specified either explicitly or by
        reference to those specified somewhere else in the instance document.
    """


class AdjustableDates(BaseModel):
    """ A class for defining a series of dates that shall be subject to
        adjustment if they would otherwise fall on a day that is not a business
        day in the specified business centers, together with the convention for
        adjusting the dates.
    """

    unadjustedDate: List[date] = Field(
        ...,
        description='A date subject to adjustment.'
    )
    """ (1..*) A date subject to adjustment. """

    dateAdjustments: BusinessDayAdjustments = Field(
        ...,
        description='The business day convention and financial business centers'
                    'used for adjusting the date if it would otherwise fall on '
                    'a day that is not a business date in the specified '
                    'business centers.'
    )
    """ (1..1) The business day convention and financial business centers
        used for adjusting the date if it would otherwise fall on a day that is
        not a business date in the specified business centers.
    """
    adjustedDate: Optional[List[date]] = Field(
        None,
        description='The date(s) once the adjustment has been performed. (Note '
                    'that this date may change if the business center holidays '
                    'change).'
    )
    """ (0..*) The date(s) once the adjustment has been performed. (Note that
        this date may change if the business center holidays change).
    """

    @validator('unadjustedDate')
    @classmethod
    def cardinality_unadjustedDate(cls, val):
        if not val:
            raise ValueError('At least one elemnt needed!')
        return val


class Frequency(BaseModel):
    """ A class for defining a date frequency, e.g. one day, three months,
        through the combination of an integer value and a standardized period
        value that is specified as part of an enumeration.
    """

    periodMultiplier: int = Field(
        ...,
        description='A time period multiplier, e.g. 1, 2, or 3. If the period '
                    'value is T (Term) then period multiplier must contain the '
                    'value 1.'
    )
    """ A time period multiplier, e.g. 1, 2, or 3. If the period value is T
       (Term) then period multiplier must contain the value 1.
    """
    period: PeriodExtendedEnum = Field(
        ...,
        description='A time period, e.g. a day, week, month, year or term of '
                    'the stream.'
    )
    """ A time period, e.g. a day, week, month, year or term of  the stream.
    """

# EOF
