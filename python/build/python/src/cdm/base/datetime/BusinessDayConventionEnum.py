from enum import Enum

all = ['BusinessDayConventionEnum']
  
class BusinessDayConventionEnum(Enum):
  """
  The enumerated values to specify the convention for adjusting any relevant date if it would otherwise fall on a day that is not a valid business day.
  """
  FOLLOWING = "FOLLOWING"
  """
  The non-business date will be adjusted to the first following day that is a business day
  """
  FRN = "FRN"
  """
  Per 2000 ISDA Definitions, Section 4.11. FRN Convention; Eurodollar Convention. FRN is included here as a type of business day convention although it does not strictly fall within ISDA's definition of a Business Day Convention and does not conform to the simple definition given above.
  """
  MODFOLLOWING = "MODFOLLOWING"
  """
  The non-business date will be adjusted to the first following day that is a business day unless that day falls in the next calendar month, in which case that date will be the first preceding day that is a business day.
  """
  MODPRECEDING = "MODPRECEDING"
  """
  The non-business date will be adjusted to the first preceding day that is a business day unless that day falls in the previous calendar month, in which case that date will be the first following day that us a business day.
  """
  NEAREST = "NEAREST"
  """
  The non-business date will be adjusted to the nearest day that is a business day - i.e. if the non-business day falls on any day other than a Sunday or a Monday, it will be the first preceding day that is a business day, and will be the first following business day if it falls on a Sunday or a Monday.
  """
  NONE = "NONE"
  """
  The date will not be adjusted if it falls on a day that is not a business day.
  """
  NOT_APPLICABLE = "NOT_APPLICABLE"
  """
  The date adjustments conventions are defined elsewhere, so it is not required to specify them here.
  """
  PRECEDING = "PRECEDING"
  """
  The non-business day will be adjusted to the first preceding day that is a business day.
  """
