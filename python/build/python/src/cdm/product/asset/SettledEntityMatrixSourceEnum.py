from enum import Enum

all = ['SettledEntityMatrixSourceEnum']
  
class SettledEntityMatrixSourceEnum(Enum):
  """
  The enumerated values to specify the relevant settled entity matrix source.
  """
  CONFIRMATION_ANNEX = "CONFIRMATION_ANNEX"
  """
  The Relevant Settled Entity Matrix shall be the list agreed for this purpose by the parties. The list is not included as part of the electronic confirmation.
  """
  NOT_APPLICABLE = "NOT_APPLICABLE"
  """
  The term is not applicable.
  """
  PUBLISHER = "PUBLISHER"
  """
  The Settled Entity Matrix published by the Index Publisher.
  """
