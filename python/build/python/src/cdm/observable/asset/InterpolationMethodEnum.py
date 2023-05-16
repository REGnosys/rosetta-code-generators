from enum import Enum

all = ['InterpolationMethodEnum']
  
class InterpolationMethodEnum(Enum):
  """
  The enumerated values to specify the interpolation method, e.g. linear.
  """
  LINEAR = "LINEAR"
  """
  Linear Interpolation applicable.
  """
  LINEAR_ZERO_YIELD = "LINEAR_ZERO_YIELD"
  """
  Linear Interpolation applicable.
  """
  NONE = "NONE"
  """
  No Interpolation applicable.
  """
