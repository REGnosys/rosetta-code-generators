from enum import Enum

all = ['ResetRelativeToEnum']
  
class ResetRelativeToEnum(Enum):
  """
  The enumerated values to specify whether resets occur relative to the first or last day of a calculation period.
  """
  CALCULATION_PERIOD_END_DATE = "CALCULATION_PERIOD_END_DATE"
  """
  Resets occur relative to the last day of a calculation period.
  """
  CALCULATION_PERIOD_START_DATE = "CALCULATION_PERIOD_START_DATE"
  """
  Resets occur relative to the first day of a calculation period.
  """
