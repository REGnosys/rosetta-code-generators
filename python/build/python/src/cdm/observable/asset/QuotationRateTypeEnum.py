from enum import Enum

all = ['QuotationRateTypeEnum']
  
class QuotationRateTypeEnum(Enum):
  """
  The enumerated values to specify the type of quotation rate to be obtained from each cash settlement reference bank.
  """
  ASK = "ASK"
  """
  An ask rate.
  """
  BID = "BID"
  """
  A bid rate.
  """
  EXERCISING_PARTY_PAYS = "EXERCISING_PARTY_PAYS"
  """
  If optional early termination is applicable to a swap transaction, the rate, which may be a bid or ask rate, which would result, if seller is in-the-money, in the higher absolute value of the cash settlement amount, or, is seller is out-of-the-money, in the lower absolute value of the cash settlement amount.
  """
  MID = "MID"
  """
  A mid-market rate.
  """
