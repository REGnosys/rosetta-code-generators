from enum import Enum

all = ['CsaTypeEnum']
  
class CsaTypeEnum(Enum):
  """
  How is the Creadit Support Annex defined for this transaction as defined in the 2021 ISDA Definitions, section 18.2.1 
  """
  EXISTING_CSA = "ExistingCSA"
  """
  Thre is an existing Credit Support Annex
  """
  NO_CSA = "NoCSA"
  """
  There is no CSA applicable
  """
  REFERENCE_VMCSA = "ReferenceVMCSA"
  """
  There is a bilateral Credit Support Annex specific to the transaction
  """
