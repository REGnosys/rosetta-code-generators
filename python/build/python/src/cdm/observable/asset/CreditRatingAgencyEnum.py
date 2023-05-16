from enum import Enum

all = ['CreditRatingAgencyEnum']
  
class CreditRatingAgencyEnum(Enum):
  """
  Represents the enumerated values to specify the rating agencies.
  """
  AM_BEST = "AM_BEST"
  """
  A. M. Best
  """
  CBRS = "CBRS"
  """
  Canadian Bond Rating Service
  """
  DBRS = "DBRS"
  """
  Dominion Bond Rating Service
  """
  FITCH = "FITCH"
  """
  Fitch
  """
  JAPANAGENCY = "JAPANAGENCY"
  """
  Japan Credit Rating Agency, Ltd.
  """
  MOODYS = "MOODYS"
  """
  Moody's
  """
  RATING_AND_INVESTMENT_INFORMATION = "RATING_AND_INVESTMENT_INFORMATION"
  """
  Rating And Investment Information, Inc.
  """
  STANDARD_AND_POORS = "STANDARD_AND_POORS"
  """
  Standard And Poor's
  """
