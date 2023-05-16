from enum import Enum

all = ['SupraNationalIssuerTypeEnum']
  
class SupraNationalIssuerTypeEnum(Enum):
  """
  Represents an enumeration list to identify the type of supranational entity issuing the asset.
  """
  INTERNATIONAL_ORGANISATION = "INTERNATIONAL_ORGANISATION"
  """
  Specifies International Financial Institution.
  """
  MULTILATERAL_BANK = "MULTILATERAL_BANK"
  """
  Specifies Multilateral Bank or Multilateral Development Bank.
  """
