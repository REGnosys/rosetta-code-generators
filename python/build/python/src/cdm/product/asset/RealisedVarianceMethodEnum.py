from enum import Enum

all = ['RealisedVarianceMethodEnum']
  
class RealisedVarianceMethodEnum(Enum):
  """
  The contract specifies which price must satisfy the boundary condition.  Used for variance, volatility and correlation caps and floors.
  """
  BOTH = "BOTH"
  """
  For a return on day T, the observed prices on both T and T-1 must be in range
  """
  LAST = "LAST"
  """
  For a return on day T, the observed price on T must be in range.
  """
  PREVIOUS = "PREVIOUS"
  """
  For a return on day T, the observed price on T-1 must be in range.
  """
