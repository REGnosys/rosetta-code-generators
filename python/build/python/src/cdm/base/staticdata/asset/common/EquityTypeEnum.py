from enum import Enum

all = ['EquityTypeEnum']
  
class EquityTypeEnum(Enum):
  """
  Represents an enumeration list to identify the type of Equity.
  """
  NON_CONVERTIBLE_PREFERENCE = "NON_CONVERTIBLE_PREFERENCE"
  """
  Identifies an Equity of Non-Convertible Preference, Shares which hold priority to receive capital return in event of issuer liquidation.
  """
  ORDINARY = "ORDINARY"
  """
  Identifies an Equity of Common stocks and shares.
  """
