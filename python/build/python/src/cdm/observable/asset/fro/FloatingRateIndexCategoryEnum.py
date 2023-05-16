from enum import Enum

all = ['FloatingRateIndexCategoryEnum']
  
class FloatingRateIndexCategoryEnum(Enum):
  """
  Top level ISDA FRO category.
  """
  CALCULATED = "Calculated Rate"
  """
  The rate is calculated by the calculation agents from multiple observations.
  """
  REFERENCE_BANKS = "Reference Banks Rate"
  """
  The rate is obtained by polling several other banks.
  """
  SCREEN_RATE = "Screen Rate"
  """
  The rate is observed directly from a screen.
  """
