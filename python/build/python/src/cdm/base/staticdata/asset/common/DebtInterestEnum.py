from enum import Enum

all = ['DebtInterestEnum']
  
class DebtInterestEnum(Enum):
  """
  Represents an enumeration list that specifies the general rule for periodic interest rate payment.
  """
  FIXED = "FIXED"
  """
  Denotes payment calculated with reference to a fixed interest rate.
  """
  FLOATING = "FLOATING"
  """
  Denotes payment calculated with reference to a floating interest rate.
  """
  INDEX_LINKED = "INDEX_LINKED"
  """
  Denotes payment calculated with reference to one or more price or other indices (other than inflation rates).
  """
  INFLATION_LINKED = "INFLATION_LINKED"
  """
  Denotes payment calculated with reference to one or more specified inflation rates.
  """
  INTEREST_ONLY = "INTEREST_ONLY"
  """
  Denotes a stripped bond representing only the interest component.
  """
  INVERSE_FLOATING = "INVERSE_FLOATING"
  """
  Denotes payment calculated with reference to the inverse of a floating interest rate.
  """
  OTHER_STRUCTURED = "OTHER_STRUCTURED"
  """
  Denotes payment calculated with reference to other underlyings (not being floating interest rates, inflation rates or indices) or with a non-linear relationship to floating interest rates, inflation rates or indices.
  """
  ZERO_COUPON = "ZERO_COUPON"
  """
  Denotes a zero coupon bond that does not pay intetrest.
  """
