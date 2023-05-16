from enum import Enum

all = ['GrossOrNetEnum']
  
class GrossOrNetEnum(Enum):
  """
  The enumerated values to specify whether price is Gross, Net or a Commission.
  """
  COMMISSION = "COMMISSION"
  """
  Denotes the amount of commission on the trade.
  """
  GROSS = "GROSS"
  """
  Denotes a negotiated price for a security or listed product, including as applicable any commissions, discounts, accrued interest, and rebates.
  """
  NET = "NET"
  """
  Denotes a negotiated price for a security or listed product, excluding as applicable any commissions, discounts, accrued interest, and rebates.
  """
