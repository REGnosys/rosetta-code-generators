from enum import Enum

all = ['DebtSeniorityEnum']
  
class DebtSeniorityEnum(Enum):
  """
  Specifies the order of repayment in the event of a sale or bankruptcy of the issuer or a related party (eg guarantor).
  """
  SECURED = "SECURED"
  """
  Denotes debt which is secured over assets of the issuer or a related party (eg guarantor).
  """
  SENIOR = "SENIOR"
  """
  Denotes debt  which ranks pari passu with all other unsecured creditors of the issuer.
  """
  SUBORDINATED = "SUBORDINATED"
  """
  Denotes debt  owed to an unsecured creditor that in the event of a liquidation can only be paid after the claims of secured and senior creditors have been met.
  """
