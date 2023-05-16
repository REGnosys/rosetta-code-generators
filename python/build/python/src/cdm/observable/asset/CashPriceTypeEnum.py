from enum import Enum

all = ['CashPriceTypeEnum']
  
class CashPriceTypeEnum(Enum):
  """
  Provides a list of possible types of cash prices, applicable when PriceTypeEnum is itself of type CashPrice.
  """
  DISCOUNT = "DISCOUNT"
  """
  Denotes a discount factor expressed as a decimal, e.g. 0.95.
  """
  FEE = "FEE"
  """
  A generic term for describing a non-scheduled cashflow that can be associated either with the initial contract, with some later corrections to it (e.g. a correction to the day count fraction that has a cashflow impact) or with some lifecycle events. Fees that are specifically associated with termination and partial termination, increase, amendment, and exercise events are qualified accordingly.
  """
  PREMIUM = "PREMIUM"
  """
  Denotes the amount payable by the buyer to the seller for an option. The premium is paid on the specified premium payment date or on each premium payment date if specified.
  """
