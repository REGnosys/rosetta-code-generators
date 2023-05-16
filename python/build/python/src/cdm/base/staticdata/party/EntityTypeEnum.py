from enum import Enum

all = ['EntityTypeEnum']
  
class EntityTypeEnum(Enum):
  """
  The enumerated values to specify the reference entity types corresponding to a list of types defined in the ISDA First to Default documentation.
  """
  ASIAN = "ASIAN"
  """
  Entity Type of Asian.
  """
  AUSTRALIAN_AND_NEW_ZEALAND = "AUSTRALIAN_AND_NEW_ZEALAND"
  """
  Entity Type of Australian and New Zealand.
  """
  EUROPEAN_EMERGING_MARKETS = "EUROPEAN_EMERGING_MARKETS"
  """
  Entity Type of European Emerging Markets.
  """
  JAPANESE = "JAPANESE"
  """
  Entity Type of Japanese.
  """
  NORTH_AMERICAN_HIGH_YIELD = "NORTH_AMERICAN_HIGH_YIELD"
  """
  Entity Type of North American High Yield.
  """
  NORTH_AMERICAN_INSURANCE = "NORTH_AMERICAN_INSURANCE"
  """
  Entity Type of North American Insurance.
  """
  NORTH_AMERICAN_INVESTMENT_GRADE = "NORTH_AMERICAN_INVESTMENT_GRADE"
  """
  Entity Type of North American Investment Grade.
  """
  SINGAPOREAN = "SINGAPOREAN"
  """
  Entity Type of Singaporean.
  """
  WESTERN_EUROPEAN = "WESTERN_EUROPEAN"
  """
  Entity Type of Western European.
  """
  WESTERN_EUROPEAN_INSURANCE = "WESTERN_EUROPEAN_INSURANCE"
  """
  Entity Type of Western European Insurance.
  """
