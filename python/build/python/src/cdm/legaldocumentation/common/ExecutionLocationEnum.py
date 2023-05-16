from enum import Enum

all = ['ExecutionLocationEnum']
  
class ExecutionLocationEnum(Enum):
  """
  The enumerated values to specify the Execution Location of a Security Agreement
  """
  EXECUTED_IN_BELGIUM = "EXECUTED_IN_BELGIUM"
  """
  The Agreement was executed outside of Belgium
  """
  EXECUTED_OUTSIDE_BELGIUM = "EXECUTED_OUTSIDE_BELGIUM"
  """
  The Agreement was executed outside of Belgium
  """
  OTHER_LOCATION = "OTHER_LOCATION"
  """
  An alternative approach is described in the document as follows.
  """
