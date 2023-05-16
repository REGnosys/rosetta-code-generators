from enum import Enum

all = ['CreditSupportAgreementTypeEnum']
  
class CreditSupportAgreementTypeEnum(Enum):
  """
  The enumerated values to specify the type of Credit Support Agreement governing the transaction.
  """
  COLLATERAL_TRANSFER_AGREEMENT = "COLLATERAL_TRANSFER_AGREEMENT"
  """
  A Collateral Transfer Agreement
  """
  CREDIT_SUPPORT_ANNEX = "CREDIT_SUPPORT_ANNEX"
  """
  A Credit Support Annex legal agreement.
  """
  CREDIT_SUPPORT_DEED = "CREDIT_SUPPORT_DEED"
  """
  A Credit Support Deed legal agreement.
  """
