""" Basic maths concepts: quantity and unit, rounding, curve / schedule,
    non-negativity constraint etc.
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case, the example reflects the first enum from
# base-math-enum.rosetta
from enum import Enum

__all__ = ['CapacityUnitEnum']


class CapacityUnitEnum(str, Enum):
    """ Provides enumerated values for capacity units, generally used in the
        context of defining quantities for commodities.
    """
    ALW = 'ALW'
    """ Denotes Allowances as standard unit.
    """
    BBL = 'BBL'
    """ Denotes a Barrel as a standard unit.
    """
    BCF = 'BCF'
    """ Denotes Billion Cubic Feet as a standard unit.
    """

# EOF
