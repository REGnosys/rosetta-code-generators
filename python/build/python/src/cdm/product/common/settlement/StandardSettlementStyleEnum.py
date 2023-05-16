from enum import Enum

all = ['StandardSettlementStyleEnum']
  
class StandardSettlementStyleEnum(Enum):
  """
  The enumerated values to specify whether a trade is settling using standard settlement instructions as well as whether it is a candidate for settlement netting.
  """
  NET = "NET"
  """
  This trade is a candidate for settlement netting.
  """
  STANDARD = "STANDARD"
  """
  This trade will settle using standard predetermined funds settlement instructions.
  """
  STANDARD_AND_NET = "STANDARD_AND_NET"
  """
  This trade will settle using standard predetermined funds settlement instructions and is a candidate for settlement netting.
  """
