from enum import Enum

all = ['FundProductTypeEnum']
  
class FundProductTypeEnum(Enum):
  """
  Represents an enumeration list to identify the fund product type.
  """
  EXCHANGE_TRADED_FUND = "EXCHANGE_TRADED_FUND"
  """
  Denotes an investment fund consisting of stocks, bonds, and/or other assets that is passively managed and traded on a stock exchange.
  """
  MONEY_MARKET_FUND = "MONEY_MARKET_FUND"
  """
  Denotes a fund that invests only in highly liquid near-term instruments such as cash, cash equivalent securities, and high credit rating debt instruments with a short-term maturity.
  """
  MUTUAL_FUND = "MUTUAL_FUND"
  """
  Denotes an investment fund consisting of stocks, bonds, and/or other assets that is actively managed and can only be purchased or sold through the investment manager.
  """
  OTHER_FUND = "OTHER_FUND"
  """
  Denotes a fund that is not an Exchange Traded Fund, Money Market Fund or Mutual Fund.
  """
