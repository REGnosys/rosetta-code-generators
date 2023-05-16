from enum import Enum

all = ['DeliveryAmountElectionEnum']
  
class DeliveryAmountElectionEnum(Enum):
  """
  The enumerated values to specify the application of Interest Amount with respect to the Delivery Amount through standard language. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).
  """
  LAST_AND_ANY_LOCAL_BUSINESS_DAY = "LAST_AND_ANY_LOCAL_BUSINESS_DAY"
  """
  The delivery includes both `Transfer on last Local Business Day` and `Transfer a Delivery Amount (IM) consisting of cash on any Local Business Day.`
  """
  LAST_LOCAL_BUSINESS_DAY = "LAST_LOCAL_BUSINESS_DAY"
  """
  The delivery only includes `Transfer on last Local Business Day`. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).
  """
