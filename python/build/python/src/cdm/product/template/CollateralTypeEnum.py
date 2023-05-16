from enum import Enum

all = ['CollateralTypeEnum']
  
class CollateralTypeEnum(Enum):
  """
  Specifies the types of collateral that are accepted by the Lender
  """
  CASH = "CASH"
  """
  Security Lending Trades against Cash collateral
  """
  CASH_POOL = "CASH_POOL"
  """
  Security Lending Trades against CashPool collateral
  """
  NON_CASH = "NON_CASH"
  """
  Security Lending Trades against NonCash collateral
  """
