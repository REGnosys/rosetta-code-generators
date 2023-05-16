from enum import Enum

all = ['ConfirmationStatusEnum']
  
class ConfirmationStatusEnum(Enum):
  """
  Enumeration for the different types of confirmation status.
  """
  CONFIRMED = "CONFIRMED"
  UNCONFIRMED = "UNCONFIRMED"
