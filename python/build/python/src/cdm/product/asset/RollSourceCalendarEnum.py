from enum import Enum

all = ['RollSourceCalendarEnum']
  
class RollSourceCalendarEnum(Enum):
  """
  Used in conjunction with an exchange-based pricing source. Identifies a date source calendar from which the pricing dates and thus roll to the next contract will be based off (e.g. pricing is based on the NYMEX WTI First Nearby Futures Contract, if Future is chosen, the pricing will roll to the next futures contract on expiration, if ListedOption is chosen, the pricing will roll to the next futures contract on the Option expiration date which is three business days before the expiration of the NYMEX WTI futures contract.) Omitting this element will result in the default behavior expected with the pricing source described within the commodity element.
  """
  FUTURE = "FUTURE"
  LISTED_OPTION = "LISTED_OPTION"
