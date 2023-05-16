from enum import Enum

all = ['CapFloorEnum']
  
class CapFloorEnum(Enum):
  """
  The enumerated values to specify whether a level is a Cap or Floor.
  """
  CAP = "CAP"
  """
  Denotes the maximum allowable level of a floating rate for the calculation period, which is used for a cap rate contractual product or in the context of a floating leg.  The CapRate is assumed to be exclusive of any spread, and is defined as a per annum rate expressed as a decimal, for example, the value of 0.05 is the equivalent of 5.0%.
  """
  FLOOR = "FLOOR"
  """
  Denotes the minimum allowable level of a floating rate for the calculation period. Can be used for a floor rate contractual product or in the context of a floating leg. The cap rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal.  For example, a floorRate value of 0.05 is the equivalent of 5.0%.
  """
