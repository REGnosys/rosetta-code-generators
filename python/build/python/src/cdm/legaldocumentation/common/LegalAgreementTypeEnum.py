from enum import Enum

all = ['LegalAgreementTypeEnum']
  
class LegalAgreementTypeEnum(Enum):
  """
  The enumerated values to specify the legal agreement type.
  """
  BROKER_CONFIRMATION = "BROKER_CONFIRMATION"
  """
  A Broker Confirmation.
  """
  CONFIRMATION = "CONFIRMATION"
  """
  A Transaction Confirmation.
  """
  CREDIT_SUPPORT_AGREEMENT = "CREDIT_SUPPORT_AGREEMENT"
  """
  A Credit Support Agreement.
  """
  MASTER_AGREEMENT = "MASTER_AGREEMENT"
  """
  A Master Agreement.
  """
  MASTER_CONFIRMATION = "MASTER_CONFIRMATION"
  """
  A Master Confirmation.
  """
  OTHER = "OTHER"
  """
  Another type of agreement.
  """
  SECURITY_AGREEMENT = "SECURITY_AGREEMENT"
  """
  A Security Agreement related to a Collateral Transfer Agreement (CTA).
  """
