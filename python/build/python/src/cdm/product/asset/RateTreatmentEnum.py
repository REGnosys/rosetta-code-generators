from enum import Enum

all = ['RateTreatmentEnum']
  
class RateTreatmentEnum(Enum):
  """
  The enumerated values to specify the methods for converting rates from one basis to another.
  """
  BOND_EQUIVALENT_YIELD = "BOND_EQUIVALENT_YIELD"
  """
  Bond Equivalent Yield. Per Annex to the 2000 ISDA Definitions (June 2000 Version), Section 7.3. Certain General Definitions Relating to Floating Rate Options, paragraph (g).
  """
  MONEY_MARKET_YIELD = "MONEY_MARKET_YIELD"
  """
  Money Market Yield. Per Annex to the 2000 ISDA Definitions (June 2000 Version), Section 7.3. Certain General Definitions Relating to Floating Rate Options, paragraph (h).
  """
