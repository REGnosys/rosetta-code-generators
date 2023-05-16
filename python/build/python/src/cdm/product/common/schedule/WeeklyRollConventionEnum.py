from enum import Enum

all = ['WeeklyRollConventionEnum']
  
class WeeklyRollConventionEnum(Enum):
  """
  The enumerated values to specify the weekly roll day.
  """
  FRI = "FRI"
  """
  Friday
  """
  MON = "MON"
  """
  Monday
  """
  SAT = "SAT"
  """
  Saturday
  """
  SUN = "SUN"
  """
  Sunday
  """
  TBILL = "TBILL"
  """
  13-week and 26-week U.S. Treasury Bill Auction Dates. Each Monday except for U.S. (New York) holidays when it will occur on a Tuesday
  """
  THU = "THU"
  """
  Thursday
  """
  TUE = "TUE"
  """
  Tuesday
  """
  WED = "WED"
  """
  Wednesday
  """
