from enum import Enum

all = ['CreditNotationMismatchResolutionEnum']
  
class CreditNotationMismatchResolutionEnum(Enum):
  """
  Represents and enumeration list to identify the characteritics of the rating if there are several agency issue ratings but not equivalent, reference will be made to label characteritics of the rating such as the lowest/highest available.
  """
  AVERAGE = "AVERAGE"
  """
  Denotes the average credit notation if several notations are listed 
  """
  HIGHEST = "HIGHEST"
  """
  Denotes the highest credit notation if several notations are listed.
  """
  LOWEST = "LOWEST"
  """
  Denotes the lowest credit notation if several notations are listed.
  """
  REFERENCE_AGENCY = "REFERENCE_AGENCY"
  """
  Denotes that a credit notation issued from a defined reference agency is used if several notations are listed.
  """
  SECOND_BEST = "SECOND_BEST"
  """
  Denotes the second best credit notaiton if several notatons are listed
  """
