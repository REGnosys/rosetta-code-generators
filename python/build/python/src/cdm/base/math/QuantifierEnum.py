from enum import Enum

all = ['QuantifierEnum']
  
class QuantifierEnum(Enum):
  """
  Represents the enumerated values to specify a logical quantification, i.e. either All or Any.
  """
  ALL = "ALL"
  """
  Specifies that the condition in the scope of the quantifier is true of every member of the domain i.e. every one of the elements in scope.
  """
  ANY = "ANY"
  """
  Specifies that the condition in the scope of the quantifier is true of at least one member of the domain i.e. one or more of the elements in scope.
  """
