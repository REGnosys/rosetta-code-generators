from enum import Enum

all = ['TriggerTimeTypeEnum']
  
class TriggerTimeTypeEnum(Enum):
  """
  The enumerated values to specify the time of day which would be considered for valuing the knock event.
  """
  ANYTIME = "ANYTIME"
  """
  At any time during the Knock Determination period (continuous barrier).
  """
  CLOSING = "CLOSING"
  """
  The close of trading on a day would be considered for valuation.
  """
