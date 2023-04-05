""" Basic date and time concepts: relative date, date range, offset, business
    centre etc.
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case, the example reflects the first enum from
# base-math-enum.rosetta
from enum import Enum

__all__ = ['PeriodExtendedEnum']


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

# EOF
