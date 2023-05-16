from enum import Enum

all = ['ExecutionTypeEnum']
  
class ExecutionTypeEnum(Enum):
  """
  The enumerated values to specify how a contract has been executed, e.g. electronically, verbally, ...
  """
  ELECTRONIC = "ELECTRONIC"
  """
  Execution via electronic execution facility, derivatives contract market, or other electronic message such as an instant message.
  """
  OFF_FACILITY = "OFF_FACILITY"
  """
  Bilateral execution between counterparties not pursuant to the rules of a SEF or DCM.
  """
