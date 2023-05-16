from enum import Enum

all = ['DayDistributionEnum']
  
class DayDistributionEnum(Enum):
  """
  Denotes the method by which the pricing days are distributed across the pricing period.
  """
  ALL = "ALL"
  FIRST = "FIRST"
  LAST = "LAST"
  PENULTIMATE = "PENULTIMATE"
