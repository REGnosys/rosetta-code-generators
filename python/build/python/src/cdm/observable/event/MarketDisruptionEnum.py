from enum import Enum

all = ['MarketDisruptionEnum']
  
class MarketDisruptionEnum(Enum):
  """
  The enumerated values to specify the handling of an averaging date market disruption for an equity derivative transaction.
  """
  MODIFIED_POSTPONEMENT = "MODIFIED_POSTPONEMENT"
  """
  As defined in section 6.7 paragraph (c) sub-paragraph (iii) of the ISDA 2002 Equity Derivative definitions.
  """
  OMISSION = "OMISSION"
  """
  As defined in section 6.7 paragraph (c) sub-paragraph (i) of the ISDA 2002 Equity Derivative definitions.
  """
  POSTPONEMENT = "POSTPONEMENT"
  """
  As defined in section 6.7 paragraph (c) sub-paragraph (ii) of the ISDA 2002 Equity Derivative definitions.
  """
