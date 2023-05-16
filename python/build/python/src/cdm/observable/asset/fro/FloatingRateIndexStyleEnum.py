from enum import Enum

all = ['FloatingRateIndexStyleEnum']
  
class FloatingRateIndexStyleEnum(Enum):
  """
  Second level ISDA FRO category.
  """
  AVERAGE_FRO = "Average FRO"
  """
  An ISDA-defined calculated rate done using arithmetic averaging.
  """
  COMPOUNDED_FRO = "Compounded FRO"
  """
  An ISDA-defined calculated rate done using arithmetic averaging.
  """
  COMPOUNDED_INDEX = "Compounded Index"
  """
  A published index calculated using compounding.
  """
  INDEX = "Index"
  """
  A published index using a methodology defined by the publisher, e.g. S&P 500.
  """
  OTHER = "Other FRO"
  OVERNIGHT = "Overnight Rate"
  PUBLISHED_AVERAGE = "Published Average Rate"
  """
   A published rate computed using an averaging methodology.
  """
  SWAP_RATE = "Swap Rate"
  """
  A rate representing the market rate for swaps of a given maturity.
  """
  TERM_RATE = "Term Rate"
  """
  A rate specified over a given term, such as a libor-type rate.
  """
