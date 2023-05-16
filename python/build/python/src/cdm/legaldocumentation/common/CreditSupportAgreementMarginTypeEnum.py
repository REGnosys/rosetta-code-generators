from enum import Enum

all = ['CreditSupportAgreementMarginTypeEnum']
  
class CreditSupportAgreementMarginTypeEnum(Enum):
  """
  The enumerated values to specify the type of margin for which a legal agreement is named.
  """
  INITIAL_MARGIN = "INITIAL_MARGIN"
  """
  Denotes a margin agreement that is identified for use with Initial Margin/IM.
  """
  VARIATION_MARGIN = "VARIATION_MARGIN"
  """
  Denotes a margin agreement that is identified for use with Variation Margin/VM.
  """
