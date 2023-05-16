from enum import Enum

all = ['AveragingCalculationMethodEnum']
  
class AveragingCalculationMethodEnum(Enum):
  """
  Specifies enumerations for the type of averaging calculation.
  """
  ARITHMETIC = "ARITHMETIC"
  """
  Refers to the calculation of an average by taking the sum of observations divided by the count of observations.
  """
  GEOMETRIC = "GEOMETRIC"
  """
  Refers to the calculation of an average by taking the nth root of the product of n observations.
  """
  HARMONIC = "HARMONIC"
  """
  Refers to the calculation of an average by taking the reciprocal of the arithmetic mean of the reciprocals of the observations.
  """
