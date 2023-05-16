from enum import Enum

all = ['DiscountingTypeEnum']
  
class DiscountingTypeEnum(Enum):
  """
  The enumerated values to specify the method of calculating discounted payment amounts. This enumerations combines the FpML DiscountingTypeEnum and FraDiscountingEnum enumerations.
  """
  AFMA = "AFMA"
  """
  As specified by the Australian Financial Markets Association (AFMA) OTC Financial Product Conventions. This discounting method should not be used for a trade documented under a legal framework where the 2006 ISDA Definitions have been incorporated.
  """
  FRA = "FRA"
  """
  As specified by the 2006 ISDA Definitions, Section 8.4. Discounting, paragraph (b).
  """
  FRA_YIELD = "FRA_YIELD"
  """
  As specified by the 2006 ISDA Definitions, Section 8.4. Discounting, paragraph (e).
  """
  STANDARD = "STANDARD"
  """
  As specified by the 2006 ISDA Definitions, Section 8.4. Discounting, paragraph (a).
  """
