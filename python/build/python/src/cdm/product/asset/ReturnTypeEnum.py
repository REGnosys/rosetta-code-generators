from enum import Enum

all = ['ReturnTypeEnum']
  
class ReturnTypeEnum(Enum):
  """
  The enumerated values to specify the type of return associated the equity payout.
  """
  PRICE = "PRICE"
  """
  Price return, i.e. excluding dividends.
  """
  TOTAL = "TOTAL"
  """
  Total return, i.e. including dividend and price components.
  """
