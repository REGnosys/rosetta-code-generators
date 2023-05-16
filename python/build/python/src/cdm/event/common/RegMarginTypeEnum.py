from enum import Enum

all = ['RegMarginTypeEnum']
  
class RegMarginTypeEnum(Enum):
  """
  Represents the enumeration values to specify the margin type in relation to bilateral or regulatory obligation.
  """
  NON_REG_IM = "NON_REG_IM"
  """
  Indicates Non Regulatory Initial margin or independent amount
  """
  REG_IM = "REG_IM"
  """
  Indicates Regulatory Initial Margin
  """
  VM = "VM"
  """
  Indicates Variation Margin
  """
