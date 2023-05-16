from enum import Enum

all = ['InterestShortfallCapEnum']
  
class InterestShortfallCapEnum(Enum):
  """
  The enumerated values to specify the interest shortfall cap, applicable to mortgage derivatives.
  """
  FIXED = "FIXED"
  VARIABLE = "VARIABLE"
