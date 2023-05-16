from enum import Enum

all = ['PeriodTimeEnum']
  
class PeriodTimeEnum(Enum):
  """
  The enumeration values to specify a time period containing additional values such as Term.
  """
  HOUR = "HOUR"
  """
  Period measured in hours.
  """
  MINUTE = "MINUTE"
  """
  Period measured in minutes.
  """
  SECOND = "SECOND"
  """
  Period measured in seconds.
  """
