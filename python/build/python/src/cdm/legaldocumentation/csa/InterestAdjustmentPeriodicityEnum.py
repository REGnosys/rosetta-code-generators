from enum import Enum

all = ['InterestAdjustmentPeriodicityEnum']
  
class InterestAdjustmentPeriodicityEnum(Enum):
  """
  The enumerated values to specify the interest adjustment periodicity election through standard language. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii). 
  """
  EACH_DAY = "EACH_DAY"
  """
  The interest adjustment takes place each day.
  """
  LAST_LOCAL_BUSINESS_DAY_OF_MONTH = "LAST_LOCAL_BUSINESS_DAY_OF_MONTH"
  """
  The interest adjustment takes place on the last local business day of each calendar month
  """
