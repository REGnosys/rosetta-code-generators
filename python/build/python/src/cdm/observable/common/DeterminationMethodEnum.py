from enum import Enum

all = ['DeterminationMethodEnum']
  
class DeterminationMethodEnum(Enum):
  """
  The enumerated values to specify the method according to which an amount or a date is determined.
  """
  AGREED_INITIAL_PRICE = "AGREED_INITIAL_PRICE"
  """
  Agreed separately between the parties.
  """
  AS_SPECIFIED_IN_MASTER_CONFIRMATION = "AS_SPECIFIED_IN_MASTER_CONFIRMATION"
  """
  As specified in Master Confirmation.
  """
  CALCULATION_AGENT = "CALCULATION_AGENT"
  """
  Determined by the Calculation Agent.
  """
  CLOSING_PRICE = "CLOSING_PRICE"
  """
  Official Closing Price.
  """
  DIVIDEND_CURRENCY = "DIVIDEND_CURRENCY"
  """
  Determined by the Currency of Equity Dividends.
  """
  EXPIRING_CONTRACT_LEVEL = "EXPIRING_CONTRACT_LEVEL"
  """
  The initial Index Level is the level of the Expiring Contract as provided in the Master Confirmation.
  """
  HEDGE_EXECUTION = "HEDGE_EXECUTION"
  """
  Determined by the Hedging Party.
  """
  ISSUER_PAYMENT_CURRENCY = "ISSUER_PAYMENT_CURRENCY"
  """
  Issuer Payment Currency.
  """
  NAV = "NAV"
  """
  Net Asset Value.
  """
  OSP_PRICE = "OSP_PRICE"
  """
  OSP Price.
  """
  OPEN_PRICE = "OPEN_PRICE"
  """
  Opening Price of the Market.
  """
  SETTLEMENT_CURRENCY = "SETTLEMENT_CURRENCY"
  """
  Settlement Currency.
  """
  STRIKE_DATE_DETERMINATION = "STRIKE_DATE_DETERMINATION"
  """
  Date on which the strike is determined in respect of a forward starting swap.
  """
  TWAP_PRICE = "TWAP_PRICE"
  """
  Official TWAP Price.
  """
  VWAP_PRICE = "VWAP_PRICE"
  """
  Official VWAP Price.
  """
  VALUATION_TIME = "VALUATION_TIME"
  """
  Price determined at valuation time.
  """
