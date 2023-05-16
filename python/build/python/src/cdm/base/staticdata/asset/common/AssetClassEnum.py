from enum import Enum

all = ['AssetClassEnum']
  
class AssetClassEnum(Enum):
  """
  The enumerated values to specify the FpML asset class categorization.
  """
  COMMODITY = "COMMODITY"
  """
  Commodity.
  """
  CREDIT = "CREDIT"
  """
  Credit.
  """
  EQUITY = "EQUITY"
  """
  Equity.
  """
  FOREIGN_EXCHANGE = "FOREIGN_EXCHANGE"
  """
  ForeignExchange.
  """
  INTEREST_RATE = "INTEREST_RATE"
  """
  InterestRate.
  """
