from enum import Enum

all = ['DividendEntitlementEnum']
  
class DividendEntitlementEnum(Enum):
  """
  The enumerated values to specify the date on which the receiver of the equity payout is entitled to the dividend.
  """
  EX_DATE = "EX_DATE"
  """
  Dividend entitlement is on the dividend ex-date.
  """
  RECORD_DATE = "RECORD_DATE"
  """
  Dividend entitlement is on the dividend record date.
  """
