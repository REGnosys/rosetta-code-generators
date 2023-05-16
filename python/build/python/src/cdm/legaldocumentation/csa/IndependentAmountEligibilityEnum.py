from enum import Enum

all = ['IndependentAmountEligibilityEnum']
  
class IndependentAmountEligibilityEnum(Enum):
  """
  The enumerated values to specify the instances where the independent amount eligible collateral is not defined as a set of eligible collateral assets. 
  """
  NONE = "NONE"
  """
  None.
  """
  NONE_UNLESS_SPECIFIED_IN_CONFIRMATION = "NONE_UNLESS_SPECIFIED_IN_CONFIRMATION"
  """
  None, unless otherwise specified in a Confirmation.
  """
