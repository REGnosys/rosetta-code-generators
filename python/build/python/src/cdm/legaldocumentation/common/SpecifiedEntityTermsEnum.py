from enum import Enum

all = ['SpecifiedEntityTermsEnum']
  
class SpecifiedEntityTermsEnum(Enum):
  """
  The enumerated values to specify the specified entity terms for the Event of Default or Termination Event specified.
  """
  ANY_AFFILIATE = "ANY_AFFILIATE"
  """
  Any Affiliate is a Specified Entity.
  """
  MATERIAL_SUBSIDIARY = "MATERIAL_SUBSIDIARY"
  """
  Any Material Subsidiary.
  """
  NAMED_SPECIFIED_ENTITY = "NAMED_SPECIFIED_ENTITY"
  """
  The Specified Entity is provided.
  """
  NONE = "NONE"
  """
  No Specified Entity is provided
  """
  OTHER_SPECIFIED_ENTITY = "OTHER_SPECIFIED_ENTITY"
  """
  Non standard Specified Entity terms are provided.
  """
