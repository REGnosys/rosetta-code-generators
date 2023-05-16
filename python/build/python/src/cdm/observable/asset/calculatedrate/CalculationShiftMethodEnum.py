from enum import Enum

all = ['CalculationShiftMethodEnum']
  
class CalculationShiftMethodEnum(Enum):
  """
   the specific calculation method, e.g. lookback. This enumeration is used to represent the definitions of modular calculated rates as described in the 2021 ISDA Definitions, section 7.
  """
  LOOKBACK = "LOOKBACK"
  """
  Calculations and weighting are done with respect to the calculation period, but observations are shifted back by several days.
  """
  NO_SHIFT = "NO_SHIFT"
  """
  calculations occur without any shifting, e.g. OIS Compounding/Basic Averaging style.
  """
  OBSERVATION_PERIOD_SHIFT = "OBSERVATION_PERIOD_SHIFT"
  """
  the observation period is shifted by several days prior to rate setting, and weightings are done with respect to the obseration period.
  """
  RATE_CUT_OFF = "RATE_CUT_OFF"
  """
  Calculations cut the rate off several business days prior to rate setting (Lockout).
  """
