from enum import Enum

all = ['CreditRatingCreditWatchEnum']
  
class CreditRatingCreditWatchEnum(Enum):
  """
  Represents the enumerated values to specify the credit watch rating.
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
