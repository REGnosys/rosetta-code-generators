""" Basic date and time concepts: relative date, date range, offset, business
    centre etc.
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case4, the example reflects the frequency data type from
# base-datetime-type.rosetta
from __future__ import annotations
from typing import List, Optional
from datetime import date
from pydantic import Field
from cdm.utils import *

__all__ = ['AdjustableDates']


class AdjustableDates(BaseDataClass):
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

    @cdm_condition
    def cardinality_unadjustedDate(self):
        return (self.unadjustedDate)


from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments

AdjustableDates.update_forward_refs()

# EOF
