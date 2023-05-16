from enum import Enum

all = ['AverageTradingVolumeMethodologyEnum']
  
class AverageTradingVolumeMethodologyEnum(Enum):
  """
  Indicates the type of equity average trading volume (single) the highest amount on one exchange, or (consolidated) volumes across more than one exchange.
  """
  CONSOLIDATED = "CONSOLIDATED"
  """
  Consolidated volume across more than one exchange.
  """
  SINGLE = "SINGLE"
  """
  Single, the highest amount on one exchange.
  """
