from enum import Enum

all = ['FinancialUnitEnum']
  
class FinancialUnitEnum(Enum):
  """
  Provides enumerated values for financial units, generally used in the context of defining quantities for securities.
  """
  CONTRACT = "CONTRACT"
  """
  Denotes financial contracts, such as listed futures and options.
  """
  CONTRACTUAL_PRODUCT = "CONTRACTUAL_PRODUCT"
  """
  Denotes a Contractual Product as defined in the CDM.  This unit type would be used when the price applies to the whole product, for example, in the case of a premium expressed as a cash amount.
  """
  INDEX_UNIT = "INDEX_UNIT"
  """
  Denotes a price expressed in index points, e.g. for a stock index.
  """
  LOG_NORMAL_VOLATILITY = "LOG_NORMAL_VOLATILITY"
  """
  Denotes a log normal volatility, expressed in %/month, where the percentage is represented as a decimal. For example, 0.15 means a log-normal volatility of 15% per month.
  """
  SHARE = "SHARE"
  """
  Denotes the number of units of financial stock shares.
  """
  VALUE_PER_DAY = "VALUE_PER_DAY"
  """
  Denotes a value (expressed in currency units) for a one day change in a valuation date, which is typically used for expressing sensitivity to the passage of time, also known as theta risk, or carry, or other names.
  """
  VALUE_PER_PERCENT = "VALUE_PER_PERCENT"
  """
  Denotes a value (expressed in currency units) per percent change in the underlying rate which is typically used for expressing sensitivity to volatility changes, also known as vega risk.
  """
  WEIGHT = "WEIGHT"
  """
  Denotes a quantity (expressed as a decimal value) represented the weight of a component in a basket.
  """
