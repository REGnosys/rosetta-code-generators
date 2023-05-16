from enum import Enum

all = ['SpreadScheduleTypeEnum']
  
class SpreadScheduleTypeEnum(Enum):
  """
  The enumerated values to specify a long or short spread value.
  """
  LONG = "LONG"
  """
  Represents a Long Spread Schedule. Spread schedules defined as 'Long' will be applied to Long Positions.
  """
  SHORT = "SHORT"
  """
  Represents a Short Spread Schedule. Spread schedules defined as 'Short' will be applied to Short Positions.
  """
