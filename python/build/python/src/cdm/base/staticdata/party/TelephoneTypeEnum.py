from enum import Enum

all = ['TelephoneTypeEnum']
  
class TelephoneTypeEnum(Enum):
  """
  The enumerated values to specify the type of telephone number, e.g. work vs. mobile.
  """
  FAX = "FAX"
  """
  A number used primarily for work-related facsimile transmissions.
  """
  MOBILE = "MOBILE"
  """
  A number on a mobile telephone that is often or usually used for work-related calls. This type of number can be used for urgent work related business when a work number is not sufficient to contact the person or firm.
  """
  PERSONAL = "PERSONAL"
  """
  A number used primarily for non work-related calls. (Normally this type of number would be used only as an emergency backup number, not as a regular course of business).
  """
  WORK = "WORK"
  """
  A number used primarily for work-related calls. Includes home office numbers used primarily for work purposes.
  """
