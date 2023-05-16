from enum import Enum

all = ['InstructionFunctionEnum']
  
class InstructionFunctionEnum(Enum):
  """
  The enumeration values indicating the BusinessEvent function associated input instructions.
  """
  COMPRESSION = "COMPRESSION"
  CONTRACT_FORMATION = "CONTRACT_FORMATION"
  EXECUTION = "EXECUTION"
  QUANTITY_CHANGE = "QUANTITY_CHANGE"
  RENEGOTIATION = "RENEGOTIATION"
