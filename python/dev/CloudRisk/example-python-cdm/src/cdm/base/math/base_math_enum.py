""" Basic maths concepts: quantity and unit, rounding, curve / schedule,
    non-negativity constraint etc.
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case, the example reflects the first enum from
# base-math-enum.rosetta
from enum import Enum

__all__ = ['CapacityUnitEnum', 'WeatherUnitEnum', 'FinancialUnitEnum']


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


class FinancialUnitEnum(str, Enum):
    """ Provides enumerated values for financial units, generally used in the
        context of defining quantities for securities."""
    Contract = 'Contract'
    """ Denotes financial contracts, such as listed futures and options.
    """
    ContractualProduct = 'ContractualProduct'
    """ Denotes a Contractual Product as defined in the CDM.  This unit type
        would be used when the price applies to the whole product, for example,
        in the case of a premium expressed as a cash amount.
    """
    IndexUnit = 'IndexUnit'
    """Denotes a price expressed in index points, e.g. for a stock index.
    """
    LogNormalVolatility = 'LogNormalVolatility'
    """ Denotes a log normal volatility, expressed in %/month, where the
        percentage is represented as a decimal. For example, 0.15 means a
        log-normal volatility of 15% per month.
    """
    Share = 'Share'
    """ Denotes the number of units of financial stock shares.
    """
    ValuePerDay = 'ValuePerDay'
    """ Denotes a value (expressed in currency units) for a one day change in a
        valuation date, which is typically used for expressing sensitivity to
        the passage of time, also known as theta risk, or carry, or other names.
    """
    ValuePerPercent = 'ValuePerPercent'
    """ Denotes a value (expressed in currency units) per percent change in the
        underlying rate which is typically used for expressing sensitivity to
        volatility changes, also known as vega risk.
    """
    Weight = 'Weight'
    """ Denotes a quantity (expressed as a decimal value) represented the
        weight of a component in a basket.
    """

# EOF
