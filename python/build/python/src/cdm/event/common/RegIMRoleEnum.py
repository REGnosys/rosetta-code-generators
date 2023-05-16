from enum import Enum

all = ['RegIMRoleEnum']
  
class RegIMRoleEnum(Enum):
  """
  Represents the enumeration values to specify the role of the party in relation to a regulatory initial margin call.
  """
  PLEDGOR = "PLEDGOR"
  """
  Indicates 'Pledgor' party of initial margin call.
  """
  SECURED = "SECURED"
  """
  Indicates 'Secured' party of initial margin call.
  """
