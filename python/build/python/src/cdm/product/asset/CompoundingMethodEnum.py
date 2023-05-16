from enum import Enum

all = ['CompoundingMethodEnum']
  
class CompoundingMethodEnum(Enum):
  """
  The enumerated values to specify the type of compounding, e.g. flat, straight.
  """
  FLAT = "FLAT"
  """
  Flat compounding. Compounding excludes the spread. Note that the first compounding period has it's interest calculated including any spread then subsequent periods compound this at a rate excluding the spread.
  """
  NONE = "NONE"
  """
  No compounding is to be applied.
  """
  SPREAD_EXCLUSIVE = "SPREAD_EXCLUSIVE"
  """
  Spread Exclusive compounding.
  """
  STRAIGHT = "STRAIGHT"
  """
  Straight compounding. Compounding includes the spread.
  """
