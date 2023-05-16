from enum import Enum

all = ['ArithmeticOperationEnum']
  
class ArithmeticOperationEnum(Enum):
  """
  An arithmetic operator that can be passed to a function
  """
  ADD = "ADD"
  """
  Addition
  """
  DIVIDE = "DIVIDE"
  """
  Division
  """
  MAX = "MAX"
  """
  Max of 2 values
  """
  MIN = "MIN"
  """
  Min of 2 values
  """
  MULTIPLY = "MULTIPLY"
  """
  Multiplication
  """
  SUBTRACT = "SUBTRACT"
  """
  Subtraction
  """
