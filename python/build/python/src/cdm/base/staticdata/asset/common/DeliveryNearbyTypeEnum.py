from enum import Enum

all = ['DeliveryNearbyTypeEnum']
  
class DeliveryNearbyTypeEnum(Enum):
  CALCULATION_PERIOD = "CALCULATION_PERIOD"
  """
  Describes the reference contract as the one that pertains to the month-year of the calculation period. If used, the nearby count is expected to be 0.
  """
  NEARBY_MONTH = "NEARBY_MONTH"
  """
  Specifies that the reference delivery date of the underlying Commodity shall be the expiration date of the futures contract in the nth nearby month.
  """
  NEARBY_WEEK = "NEARBY_WEEK"
  """
  Specifies that the reference delivery date of the underlying Commodity shall be the expiration date of the futures contract in the nth nearby week.
  """
