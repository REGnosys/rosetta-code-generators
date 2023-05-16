from enum import Enum

all = ['PerformanceTransferTypeEnum']
  
class PerformanceTransferTypeEnum(Enum):
  """
  The enumerated values to specify the origin of a performance transfer
  """
  COMMODITY = "COMMODITY"
  CORRELATION = "CORRELATION"
  DIVIDEND = "DIVIDEND"
  EQUITY = "EQUITY"
  INTEREST = "INTEREST"
  VARIANCE = "VARIANCE"
  VOLATILITY = "VOLATILITY"
