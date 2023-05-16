from enum import Enum

all = ['ExceptionEnum']
  
class ExceptionEnum(Enum):
  """
  The enumerated values to specify the normalized exceptions applicable to an Initial Margin CSA.
  """
  APPLICABLE = "APPLICABLE"
  """
  The election is applicable.
  """
  NOT_APPLICABLE = "NOT_APPLICABLE"
  """
  The exception is not applicable. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles. | ISDA 2018 Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  OTHER = "OTHER"
  """
  An alternative approach is described in the document as follows.
  """
