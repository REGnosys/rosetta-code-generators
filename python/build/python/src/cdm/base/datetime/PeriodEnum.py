from enum import Enum

all = ['PeriodEnum']
  
class PeriodEnum(Enum):
  """
  The enumerated values to specify the period, e.g. day, week.
  """
  D = "D"
  """
  Day
  """
  M = "M"
  """
  Month
  """
  W = "W"
  """
  Week
  """
  Y = "Y"
  """
  Year
  """
