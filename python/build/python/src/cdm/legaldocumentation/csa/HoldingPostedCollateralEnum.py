from enum import Enum

all = ['HoldingPostedCollateralEnum']
  
class HoldingPostedCollateralEnum(Enum):
  """
  The enumerated values to specify condition(s) required by a party from the other party to hold its posted collateral. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (h)(i): Eligibility to Hold Posted Collateral (VM); Custodians (VM).
  """
  ACCEPTABLE_CUSTODIAN = "ACCEPTABLE_CUSTODIAN"
  """
  The custodian is acceptable to the other party to the agreement.
  """
