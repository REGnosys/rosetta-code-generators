from enum import Enum

all = ['CreditRatingOutlookEnum']
  
class CreditRatingOutlookEnum(Enum):
  """
  Represents the enumerated values to specify the credit rating outlook.
  """
  DEVELOPING = "DEVELOPING"
  """
  Denotes a rating may be raised, lowered, or affirmed.
  """
  NEGATIVE = "NEGATIVE"
  """
  Denotes a rating may be lowered.
  """
  POSITIVE = "POSITIVE"
  """
  Denotes a rating may be raised.
  """
  STABLE = "STABLE"
  """
  Denotes a rating is not likely to change.
  """
