from enum import Enum

all = ['SpreadTypeEnum']
  
class SpreadTypeEnum(Enum):
  """
  The enumerated values to specify a price defined as a spread.
  """
  BASE = "BASE"
  """
  Denotes the base price against which a spread is expressed. For a foreign exchange forward trade, denotes the spot price against which forward points are expressed.
  """
  SPREAD = "SPREAD"
  """
  Denotes a difference in interest rates or prices expressed as a decimal. For example, in the case of a spread between two interest rates, the value of 0.05 is the equivalent of 500 basis points or 5.0%. For a foreign exchange forward trade, denotes the forward points to be added to a spot price to represent a forward price, expressed as a decimal.
  """
