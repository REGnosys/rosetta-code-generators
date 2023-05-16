from enum import Enum

all = ['ElectiveAmountEnum']
  
class ElectiveAmountEnum(Enum):
  """
  The enumerated values to specify an elective amount.
  """
  UNLIMITED = "UNLIMITED"
  """
  The elective amount has no upper limit.
  """
  ZERO = "ZERO"
  """
  The elective amount is zero.
  """
