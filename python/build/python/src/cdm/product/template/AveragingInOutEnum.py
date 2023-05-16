from enum import Enum

all = ['AveragingInOutEnum']
  
class AveragingInOutEnum(Enum):
  """
  The enumerated values to specify the type of averaging used in an Asian option.
  """
  BOTH = "BOTH"
  """
  The average price is used to derive both the strike and the expiration price.
  """
  IN = "IN"
  """
  The average price is used to derive the strike price. Also known as 'Asian strike' style option.
  """
  OUT = "OUT"
  """
  The average price is used to derive the expiration price. Also known as 'Asian price' style option.
  """
