from enum import Enum

all = ['ConcentrationLimitTypeEnum']
  
class ConcentrationLimitTypeEnum(Enum):
  """
  Represents the enumerated values to identify where a concentration limit is applied.
  """
  ASSET = "ASSET"
  """
  Specifies a limit on a single asset in the portfolio
  """
  BASE_CURRENCY_EQUIVALENT = "BASE_CURRENCY_EQUIVALENT"
  """
  Specifies a limit on all cash valued in the base currency of the portfolio.
  """
  INDUSTRY_SECTOR = "INDUSTRY_SECTOR"
  """
  Specifies a limit on a single industry sector in the portfolio.
  """
  ISSUE_OUTSTANDING_AMOUNT = "ISSUE_OUTSTANDING_AMOUNT"
  """
  Specifies a limit of the issue compared to the outstanding amount of the asset on the market.
  """
  ISSUER = "ISSUER"
  """
  Specifies a limit on a single issuer in the portfolio.
  """
  MARKET_CAPITALISATION = "MARKET_CAPITALISATION"
  """
  Specifies a limit of the issue calculated as a percentage of the market capitalisation of the asset on the market.
  """
  PRIMARY_EXCHANGE = "PRIMARY_EXCHANGE"
  """
  Specifies a limit on a single exchange in the portfolio.
  """
  ULTIMATE_PARENT_INSTITUTION = "ULTIMATE_PARENT_INSTITUTION"
  """
  Specifies a limit on a single issuer in the portfolio at the ultimate parent institution level.
  """
