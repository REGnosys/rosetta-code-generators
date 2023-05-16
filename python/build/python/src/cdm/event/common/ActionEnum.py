from enum import Enum

all = ['ActionEnum']
  
class ActionEnum(Enum):
  """
  The enumeration values to specify the actions associated with transactions.
  """
  CANCEL = "CANCEL"
  """
  A cancellation of a prior instance of the transaction event. The eventIdentifier has an associated version greater than 1.
  """
  CORRECT = "CORRECT"
  """
  A correction of a prior instance of the transaction event. The eventIdentifier has an associated version greater than 1.
  """
  NEW = "NEW"
  """
  A new instance of a transaction event, which is also characterized by the fact that the eventIdentifier has an associated version 1.
  """
