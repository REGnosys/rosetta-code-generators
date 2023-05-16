from enum import Enum

all = ['RestructuringEnum']
  
class RestructuringEnum(Enum):
  """
  The enumerated values to specify the form of the restructuring credit event that is applicable to the credit default swap.
  """
  MOD_MOD_R = "MOD_MOD_R"
  """
  Restructuring (Section 4.7) and Modified Restructuring Maturity Limitation and Conditionally Transferable Obligation (2014 Definitions: Section 3.31, 2003 Definitions: 2.32) apply.
  """
  MOD_R = "MOD_R"
  """
  Restructuring (Section 4.7) and Restructuring Maturity Limitation and Fully Transferable Obligation (2014 Definitions: Section 3.31, 2003 Definitions: 2.32) apply.
  """
  R = "R"
  """
  Restructuring as defined in the applicable ISDA Credit Derivatives Definitions. (2003 or 2014).
  """
