from enum import Enum

all = ['MarginCallActionEnum']
  
class MarginCallActionEnum(Enum):
  """
  Represents the enumeration values to identify the collateral action instruction.
  """
  DELIVERY = "DELIVERY"
  """
  Indicates an instruction of a new collateral asset delivery.
  """
  RETURN = "RETURN"
  """
  Indicates an instruction for a return of a principals collateral asset delivery.
  """
