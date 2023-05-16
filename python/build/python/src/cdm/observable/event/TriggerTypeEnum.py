from enum import Enum

all = ['TriggerTypeEnum']
  
class TriggerTypeEnum(Enum):
  """
  The enumerated values to specify whether an option will trigger or expire depending upon whether the spot rate is above or below the barrier rate.
  """
  EQUAL = "EQUAL"
  """
  The underlier price must be equal to the Trigger level.
  """
  EQUAL_OR_GREATER = "EQUAL_OR_GREATER"
  """
  The underlier price must be equal to or greater than the Trigger level.
  """
  EQUAL_OR_LESS = "EQUAL_OR_LESS"
  """
  The underlier price must be equal to or less than the Trigger level.
  """
  GREATER = "GREATER"
  """
  The underlier price must be greater than the Trigger level.
  """
  LESS = "LESS"
  """
  The underlier price must be less than the Trigger level.
  """
