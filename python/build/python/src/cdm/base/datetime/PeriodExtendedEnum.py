from enum import Enum

all = ['PeriodExtendedEnum']
  
class PeriodExtendedEnum(Enum):
  """
  The enumerated values to specify a time period containing the additional value of Term.
  """
  C = "C"
  """
  CalculationPeriod - the period corresponds to the calculation period   For example, used in the Commodity Markets to indicate that a reference contract is the one that corresponds to the period of the calculation period.
  """
  D = "D"
  """
  Day
  """
  H = "H"
  """
  Hour
  """
  M = "M"
  """
  Month
  """
  T = "T"
  """
  Term. The period commencing on the effective date and ending on the termination date. The T period always appears in association with periodMultiplier = 1, and the notation is intended for use in contexts where the interval thus qualified (e.g. accrual period, payment period, reset period, ...) spans the entire term of the trade.
  """
  W = "W"
  """
  Week
  """
  Y = "Y"
  """
  Year
  """
