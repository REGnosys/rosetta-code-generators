from enum import Enum

all = ['AssetTypeEnum']
  
class AssetTypeEnum(Enum):
  """
  Represents an enumeration list to identify the asset type.
  """
  CASH = "CASH"
  """
  Indentifies cash in a currency form.
  """
  COMMODITY = "COMMODITY"
  """
  Indentifies basic good used in commerce that is interchangeable with other goods of the same type.
  """
  OTHER = "OTHER"
  """
  Indentifies other asset types.
  """
  SECURITY = "SECURITY"
  """
  Indentifies negotiable financial instrument of monetary value with an issue ownership position.
  """
