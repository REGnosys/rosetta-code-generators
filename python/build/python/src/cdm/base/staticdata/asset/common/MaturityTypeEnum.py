from enum import Enum

all = ['MaturityTypeEnum']
  
class MaturityTypeEnum(Enum):
  """
  Represents an enumeration list to identify the Maturity.
  """
  FROM_ISSUANCE = "FROM_ISSUANCE"
  """
  Denotes a period from issuance date until now.
  """
  ORIGINAL_MATURITY = "ORIGINAL_MATURITY"
  """
  Denotes a period from issuance until maturity date.
  """
  REMAINING_MATURITY = "REMAINING_MATURITY"
  """
  Denotes a period from now until maturity date.
  """
