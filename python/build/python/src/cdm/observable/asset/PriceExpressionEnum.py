from enum import Enum

all = ['PriceExpressionEnum']
  
class PriceExpressionEnum(Enum):
  """
  Enumerated values to specify whether the price is expressed in absolute or relative terms.
  """
  ABSOLUTE_TERMS = "ABSOLUTE_TERMS"
  """
  The price is expressed as an absolute amount.
  """
  PAR_VALUE_FRACTION = "PAR_VALUE_FRACTION"
  """
  Denotes a price expressed in percentage of face value with fractions which is used for quoting bonds, e.g. 101 3/8 indicates that the buyer will pay 101.375 of the face value.
  """
  PER_OPTION = "PER_OPTION"
  """
  Denotes a price expressed per number of options.
  """
  PERCENTAGE_OF_NOTIONAL = "PERCENTAGE_OF_NOTIONAL"
  """
  The price is expressed in percentage of the notional amount.
  """
