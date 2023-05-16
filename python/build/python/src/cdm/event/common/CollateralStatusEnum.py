from enum import Enum

all = ['CollateralStatusEnum']
  
class CollateralStatusEnum(Enum):
  """
  Represents the enumeration list to identify the settlement status of the collateral.
  """
  FULL_AMOUNT = "FULL_AMOUNT"
  """
  Indicates the collateral balance amount in full, inclusive of any pre-agreed collateral positions in transit for settlement.
  """
  IN_TRANSIT_AMOUNT = "IN_TRANSIT_AMOUNT"
  """
  Indicates collateral amount in transit settlement cycle only, excluding settled collateral amount/s.
  """
  SETTLED_AMOUNT = "SETTLED_AMOUNT"
  """
  Indicates the collateral is settled and not an in transit pre-agreed collateral amount/s.
  """
