""" Basic maths concepts: quantity and unit, rounding, curve / schedule,
    non-negativity constraint etc.
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case, the example reflects the first enum from
# base-math-enum.rosetta
from enum import Enum

__all__ = ['WeatherUnitEnum']


class WeatherUnitEnum(str, Enum):
    """ Provides enumerated values for weather units, generally used in the
        context of defining quantities for commodities.
    """
    CDD = 'CDD'
    """ Denotes Cooling Degree Days as a standard unit.
    """
    CPD = 'CPD'
    """ Denotes Critical Precipitation Day as a standard unit.
    """
    HDD = 'HDD'
    """ Heating Degree Day as a standard unit.
    """

# EOF
