from enum import Enum

all = ['SpecifiedEntityClauseEnum']
  
class SpecifiedEntityClauseEnum(Enum):
  """
  The enumerated values to specify the Event of Default or Termination event for which Specified Entities terms are being defined.
  """
  BANKRUPTCY = "BANKRUPTCY"
  CREDIT_EVENT_UPON_MERGER = "CREDIT_EVENT_UPON_MERGER"
  CROSS_DEFAULT = "CROSS_DEFAULT"
  DEFAULT_UNDER_SPECIFIED_TRANSACTION = "DEFAULT_UNDER_SPECIFIED_TRANSACTION"
