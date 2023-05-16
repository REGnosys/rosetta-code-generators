from enum import Enum

all = ['ObservationPeriodDatesEnum']
  
class ObservationPeriodDatesEnum(Enum):
  """
  The enumerated values to specify whether rate calculations occur relative to the first or last day of a calculation period. Done in uppercase due to a bug in code generation. This enumeration is used to represent the definitions of modular calculated rates as described in the 2021 ISDA Definitions, section 7.
  """
  FIXING_DATE = "FIXING_DATE"
  """
  Calculations occur relative to a previously defined reset date, e.g. for a fallback rate.
  """
  SET_IN_ADVANCE = "SET_IN_ADVANCE"
  """
  Calculations occur relative to the first day of a calculation period.
  """
  STANDARD = "STANDARD"
  """
  Calculations occur relative to the last day of a calculation period (set in arrears).
  """
