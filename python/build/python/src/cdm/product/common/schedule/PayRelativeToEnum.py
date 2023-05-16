from enum import Enum

all = ['PayRelativeToEnum']
  
class PayRelativeToEnum(Enum):
  """
  The enumerated values to specify whether payments occur relative to the calculation period start date or end date, each reset date, valuation date or the last pricing date.
  """
  CALCULATION_PERIOD_END_DATE = "CALCULATION_PERIOD_END_DATE"
  """
  Payments will occur relative to the last day of each calculation period.
  """
  CALCULATION_PERIOD_START_DATE = "CALCULATION_PERIOD_START_DATE"
  """
  Payments will occur relative to the first day of each calculation period.
  """
  LAST_PRICING_DATE = "LAST_PRICING_DATE"
  """
  Payments will occur relative to the last Pricing Date of each Calculation Period.
  """
  RESET_DATE = "RESET_DATE"
  """
  Payments will occur relative to the reset date.
  """
  VALUATION_DATE = "VALUATION_DATE"
  """
  Payments will occur relative to the valuation date.
  """
