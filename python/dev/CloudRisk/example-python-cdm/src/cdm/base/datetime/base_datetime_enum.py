""" Basic date and time concepts: relative date, date range, offset, business
    centre etc.
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case, the example reflects the first enum from
# base-math-enum.rosetta
from enum import Enum

__all__ = [
    'PeriodExtendedEnum', 'BusinessCenterEnum', 'BusinessDayConventionEnum'
]


class PeriodExtendedEnum(str, Enum):
    """ The enumerated values to specify a time period containing the
        additional value of Term.
    """
    D = 'D'
    """ Day
    """
    W = 'W'
    """ Week
    """
    M = 'M'
    """ Month
    """
    Y = 'Y'
    """ Year
    """
    T = 'T'
    """ Term. The period commencing on the effective date and ending on the
        termination date. The T period always appears in association with
        periodMultiplier = 1, and the notation is intended for use in contexts
        where the interval thus qualified (e.g. accrual period, payment period,
        reset period, ...) spans the entire term of the trade.
    """
    C = 'C'
    """ CalculationPeriod - the period corresponds to the calculation period
        For example, used in the Commodity Markets to indicate that a reference
        contract is the one that corresponds to the period of the calculation
        period.
    """


class BusinessCenterEnum(str, Enum):
    """The enumerated values to specify the business centers."""
    # [docReference ISDA FpML_Coding_Scheme schemeLocation
    # "http://www.fpml.org/coding-scheme/business-center-8-2"]

    AEAD = 'AEAD'
    """Abu Dhabi, United Arab Emirates"""
    AEDU = 'AEDU'
    """Dubai, United Arab Emirates"""
    AMYE = 'AMYE'
    """Yerevan, Armenia"""
    AOLU = 'AOLU'
    """Luanda, Angola"""
    ARBA = 'ARBA'
    """Buenos Aires, Argentina"""


class BusinessDayConventionEnum(str, Enum):
    """ The enumerated values to specify the convention for adjusting any
        relevant date if it would otherwise fall on a day that is not a valid
        business day.
    """
    FOLLOWING = 'FOLLOWING'
    """ The non-business date will be adjusted to the first following day that
        is a business day
    """
    FRN = 'FRN'
    """ Per 2000 ISDA Definitions, Section 4.11. FRN Convention; Eurodollar
        Convention. FRN is included here as a type of business day convention
        although it does not strictly fall within ISDA's definition of a
        Business Day Convention and does not conform to the simple definition
        given above.
    """
    MODFOLLOWING = 'MODFOLLOWING'
    """ The non-business date will be adjusted to the first following day that
        is a business day unless that day falls in the next calendar month, in
        which case that date will be the first preceding day that is a business
        day.
    """
    PRECEDING = 'PRECEDING'
    """ The non-business day will be adjusted to the first preceding day that is
        a business day.
    """
    MODPRECEDING = 'MODPRECEDING'
    """ The non-business date will be adjusted to the first preceding day that
        is a business day unless that day falls in the previous calendar month,
        in which case that date will be the first following day that us a
        business day.
    """
    NEAREST = 'NEAREST'
    """ The non-business date will be adjusted to the nearest day that is a
        business day - i.e. if the non-business day falls on any day other than
        a Sunday or a Monday, it will be the first preceding day that is a
        business day, and will be the first following business day if it falls
        on a Sunday or a Monday.
    """
    NONE = 'NONE'
    """ The date will not be adjusted if it falls on a day that is not a
        business day.
    """
    NotApplicable = 'NotApplicable'
    """ The date adjustments conventions are defined elsewhere, so it is not
        required to specify them here.
    """

# EOF
