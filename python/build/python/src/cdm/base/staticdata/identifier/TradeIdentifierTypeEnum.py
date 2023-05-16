from enum import Enum

all = ['TradeIdentifierTypeEnum']
  
class TradeIdentifierTypeEnum(Enum):
  """
  Defines the enumerated values to specify the nature of a trade identifier.
  """
  UNIQUE_SWAP_IDENTIFIER = "UNIQUE_SWAP_IDENTIFIER"
  UNIQUE_TRANSACTION_IDENTIFIER = "UNIQUE_TRANSACTION_IDENTIFIER"
