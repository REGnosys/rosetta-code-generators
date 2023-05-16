from enum import Enum

all = ['DayTypeEnum']
  
class DayTypeEnum(Enum):
  """
  Lists the enumerated values to specify the day type classification used in counting the number of days between two dates.
  """
  BUSINESS = "BUSINESS"
  """
  Applies when calculating the number of days between two dates the count includes only business days.
  """
  CALENDAR = "CALENDAR"
  """
  Applies when calculating the number of days between two dates the count includes all calendar days.
  """
  CURRENCY_BUSINESS = "CURRENCY_BUSINESS"
  """
  Applies when calculating the number of days between two dates the count includes only currency business days.
  """
  EXCHANGE_BUSINESS = "EXCHANGE_BUSINESS"
  """
  Applies when calculating the number of days between two dates the count includes only stock exchange business days.
  """
  SCHEDULED_TRADING_DAY = "SCHEDULED_TRADING_DAY"
  """
  Applies when calculating the number of days between two dates the count includes only scheduled trading days.
  """
