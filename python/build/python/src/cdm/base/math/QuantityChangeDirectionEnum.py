from enum import Enum

all = ['QuantityChangeDirectionEnum']
  
class QuantityChangeDirectionEnum(Enum):
  """
  Specifies whether a quantity change is an increase, a decrease or a replacement, whereby the quantity is always specified as a positive number.
  """
  DECREASE = "DECREASE"
  """
  When the quantity should go down by the specified amount.
  """
  INCREASE = "INCREASE"
  """
  When the quantity should go up by the specified amount.
  """
  REPLACE = "REPLACE"
  """
  When the quantity should be replaced by the specified amount.
  """
