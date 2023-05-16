from enum import Enum

all = ['MarginTypeEnum']
  
class MarginTypeEnum(Enum):
  """
  This indicator defines which type of assets (cash or securities) is specified to apply as margin to the repo transaction.
  """
  CASH = "CASH"
  """
  When the margin type is Cash, the margin factor is applied to the cash value of the transaction.
  """
  INSTRUMENT = "INSTRUMENT"
  """
  When the margin type is Instrument, the margin factor is applied to the instrument value for the transaction. In the 'instrument' case, the haircut would be applied to the securities.
  """
