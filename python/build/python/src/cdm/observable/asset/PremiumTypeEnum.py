from enum import Enum

all = ['PremiumTypeEnum']
  
class PremiumTypeEnum(Enum):
  """
  The enumerated values to specify the premium type for forward start options.
  """
  FIXED = "FIXED"
  POST_PAID = "POST_PAID"
  PRE_PAID = "PRE_PAID"
  VARIABLE = "VARIABLE"
