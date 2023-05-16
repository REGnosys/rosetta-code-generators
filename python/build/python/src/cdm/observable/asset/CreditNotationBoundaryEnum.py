from enum import Enum

all = ['CreditNotationBoundaryEnum']
  
class CreditNotationBoundaryEnum(Enum):
  """
  Identifies an agency rating as a simple scale boundary of minimum or maximum.
  """
  MAXIMUM = "MAXIMUM"
  """
  Denotes a maxiumum boundary
  """
  MINIMUM = "MINIMUM"
  """
  Denotes a minumum boundary
  """
