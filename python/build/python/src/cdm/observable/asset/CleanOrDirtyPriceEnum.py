from enum import Enum

all = ['CleanOrDirtyPriceEnum']
  
class CleanOrDirtyPriceEnum(Enum):
  """
  The enumerated values to specify whether price is clean, dirty or accrued interest.
  """
  ACCRUED_INTEREST = "ACCRUED_INTEREST"
  """
  Denotes interest accrued between payments, represented as a decimal, for example the accrued interest associated with a bond trade.
  """
  CLEAN = "CLEAN"
  """
  Denotes a bond price without accrued interest.
  """
  DIRTY = "DIRTY"
  """
  Denotes a bond price with accrued interest.
  """
