from enum import Enum

all = ['FloatingRateIndexCalculationMethodEnum']
  
class FloatingRateIndexCalculationMethodEnum(Enum):
  """
  3rd level ISDA FRO category.
  """
  AVERAGE = "Overnight Average"
  """
  A calculation methodology using the arithmetic mean.
  """
  OIS_COMPOUND = "OIS Compounding"
  """
  A calculation methodology using the ISDA-defined OIS compounding formula.
  """
