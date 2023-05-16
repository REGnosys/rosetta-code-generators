from enum import Enum

all = ['QuoteBasisEnum']
  
class QuoteBasisEnum(Enum):
  """
  The enumerated values to specify how an exchange rate is quoted.
  """
  CURRENCY_1_PER_CURRENCY_2 = "CURRENCY_1_PER_CURRENCY_2"
  """
  The amount of currency1 for one unit of currency2
  """
  CURRENCY_2_PER_CURRENCY_1 = "CURRENCY_2_PER_CURRENCY_1"
  """
  The amount of currency2 for one unit of currency1
  """
