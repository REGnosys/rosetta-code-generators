from enum import Enum

all = ['QuotationStyleEnum']
  
class QuotationStyleEnum(Enum):
  """
  The enumerated values to specify the actual quotation style (e.g. PointsUpFront, TradedSpread) used to quote a credit default swap fee leg.
  """
  POINTS_UP_FRONT = "POINTS_UP_FRONT"
  """
  When quotation style is 'PointsUpFront', the initialPoints element of the Credit Default Swap feeLeg should be populated
  """
  PRICE = "PRICE"
  """
  When quotation style is 'Price', the marketPrice element of the Credit Default Swap feeLeg should be populated
  """
  TRADED_SPREAD = "TRADED_SPREAD"
  """
  When quotation style is 'TradedSpread', the marketFixedRate element of the Credit Default Swap feeLeg should be populated
  """
