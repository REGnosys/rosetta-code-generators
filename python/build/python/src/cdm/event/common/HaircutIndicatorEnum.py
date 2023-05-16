from enum import Enum

all = ['HaircutIndicatorEnum']
  
class HaircutIndicatorEnum(Enum):
  """
  Represents the enumeration indicators to specify if an asset or group of assets valuation is based on any valuation treatment haircut.
  """
  POST_HAIRCUT = "POST_HAIRCUT"
  """
  Indicates Post haircut value
  """
  PRE_HAIRCUT = "PRE_HAIRCUT"
  """
  Indicates Pre haircut value
  """
