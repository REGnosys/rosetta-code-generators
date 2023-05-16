from enum import Enum

all = ['CreditRiskEnum']
  
class CreditRiskEnum(Enum):
  """
  Represents an enumeration list to identify tranched or untranched credit risk.
  """
  TRANCHED_CREDIT_RISK = "TRANCHED_CREDIT_RISK"
  """
  Indicates tranched credit risk, including securitizations.
  """
  UNTRANCHED_CREDIT_RISK = "UNTRANCHED_CREDIT_RISK"
  """
  Indicates tranched credit risk, including repackagings.
  """
