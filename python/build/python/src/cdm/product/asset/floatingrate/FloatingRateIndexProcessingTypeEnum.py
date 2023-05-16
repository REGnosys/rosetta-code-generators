from enum import Enum

all = ['FloatingRateIndexProcessingTypeEnum']
  
class FloatingRateIndexProcessingTypeEnum(Enum):
  """
  This enumeration provides guidance on how to process a given floating rate index.  It's based on the ISDA Floating Rate Index information, but transforms it into the specific categories needed for calculation 
  """
  COMPOUND_INDEX = "COMPOUND_INDEX"
  """
  A published index calculated using compounding; the implied rate must be backed out.
  """
  MODULAR = "MODULAR"
  """
  These are calculated by the calculation agent based on deal-specific parameters (e.g. lookback compound based on an RFR).
  """
  OIS = "OIS"
  """
  These are calculated by the calculation agent based on a standard OIS FRO definition.
  """
  OVERNIGHT_AVG = "OVERNIGHT_AVG"
  """
  These are calculated by the calculation agent based on a standard overnight averaging FRO definition.
  """
  REF_BANKS = "REF_BANKS"
  """
  These must be looked up using a manual process
  """
  SCREEN = "SCREEN"
  """
  These values are just looked up from the screen and applied.
  """
