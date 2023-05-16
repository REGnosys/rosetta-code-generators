from enum import Enum

all = ['DurationTypeEnum']
  
class DurationTypeEnum(Enum):
  """
  Specifies the duration type of the Security Lending transaction. e.g. Open or Term.
  """
  EVERGREEN = "EVERGREEN"
  """
  Specifies a trade where the term date is extended by a pre-determined period until a notice is serviced. Once the notice is served, the trade will not be reset again and goes to term.
  """
  OPEN = "OPEN"
  """
  Specifies a trade with no termination date.
  """
  TERM = "TERM"
  """
  Specifies a trade with a termination date.
  """
