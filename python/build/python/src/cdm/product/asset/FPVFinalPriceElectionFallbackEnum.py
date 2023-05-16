from enum import Enum

all = ['FPVFinalPriceElectionFallbackEnum']
  
class FPVFinalPriceElectionFallbackEnum(Enum):
  """
  Specifies the fallback provisions in respect to the applicable Futures Price Valuation.
  """
  FPV_CLOSE = "FPV_CLOSE"
  """
  In respect of the Early Final Valuation Date, the provisions for FPV Close shall apply.
  """
  FPV_HEDGE_EXECUTION = "FPV_HEDGE_EXECUTION"
  """
  In respect of the Early Final Valuation Date, the provisions for FPV Hedge Execution shall apply.
  """
