from enum import Enum

all = ['ValuationMethodEnum']
  
class ValuationMethodEnum(Enum):
  """
  The enumerated values to specify the ISDA defined methodology for determining the final price of the reference obligation for purposes of cash settlement.
  """
  AVERAGE_BLENDED_HIGHEST = "AVERAGE_BLENDED_HIGHEST"
  AVERAGE_BLENDED_MARKET = "AVERAGE_BLENDED_MARKET"
  AVERAGE_HIGHEST = "AVERAGE_HIGHEST"
  AVERAGE_MARKET = "AVERAGE_MARKET"
  BLENDED_HIGHEST = "BLENDED_HIGHEST"
  BLENDED_MARKET = "BLENDED_MARKET"
  HIGHEST = "HIGHEST"
  MARKET = "MARKET"
