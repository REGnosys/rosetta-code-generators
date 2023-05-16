from enum import Enum

all = ['RecordAmountTypeEnum']
  
class RecordAmountTypeEnum(Enum):
  """
  The enumeration of the account level for the billing summary.
  """
  ACCOUNT_TOTAL = "ACCOUNT_TOTAL"
  GRAND_TOTAL = "GRAND_TOTAL"
  PARENT_TOTAL = "PARENT_TOTAL"
