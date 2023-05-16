from enum import Enum

all = ['PartyIdentifierTypeEnum']
  
class PartyIdentifierTypeEnum(Enum):
  """
  The enumeration values associated with party identifier sources.
  """
  BIC = "BIC"
  """
  The Bank Identifier Code.
  """
  LEI = "LEI"
  """
  The ISO 17442:2012 Legal Entity Identifier.
  """
  MIC = "MIC"
  """
  The ISO 10383 Market Identifier Code (MIC).
  """
