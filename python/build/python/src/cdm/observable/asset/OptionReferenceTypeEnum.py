from enum import Enum

all = ['OptionReferenceTypeEnum']
  
class OptionReferenceTypeEnum(Enum):
  """
  The enumeration values to specify the reference source that determines the final settlement price of the option.
  """
  FUTURE = "FUTURE"
  """
  Reference from the price of a future contract.
  """
  SPOT = "SPOT"
  """
  Reference from an underlyer spot price.
  """
