from enum import Enum

all = ['NonCashDividendTreatmentEnum']
  
class NonCashDividendTreatmentEnum(Enum):
  """
  The enumerated values to specify the treatment of Non-Cash Dividends.
  """
  CASH_EQUIVALENT = "CASH_EQUIVALENT"
  """
  Any non-cash dividend shall be treated as a Declared Cash Equivalent Dividend.
  """
  POTENTIAL_ADJUSTMENT_EVENT = "POTENTIAL_ADJUSTMENT_EVENT"
  """
  The treatment of any non-cash dividend shall be determined in accordance with the Potential Adjustment Event provisions.
  """
