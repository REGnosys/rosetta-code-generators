from enum import Enum

all = ['ScheduledTransferEnum']
  
class ScheduledTransferEnum(Enum):
  """
  The qualification of the type of cash flows associated with OTC derivatives contracts and their lifecycle events.
  """
  CORPORATE_ACTION = "CORPORATE_ACTION"
  """
  A cash flow corresponding to a corporate action event.
  """
  COUPON = "COUPON"
  """
  A cash flow corresponding to the periodic accrued interests.
  """
  CREDIT_EVENT = "CREDIT_EVENT"
  """
  A cashflow resulting from a credit event.
  """
  DIVIDEND_RETURN = "DIVIDEND_RETURN"
  """
  A cash flow corresponding to the synthetic dividend of an equity underlier asset traded through a derivative instrument.
  """
  EXERCISE = "EXERCISE"
  """
  A cash flow associated with an exercise lifecycle event.
  """
  FIXED_RATE_RETURN = "FIXED_RATE_RETURN"
  """
  A cash flow corresponding to the return of the fixed interest rate portion of a derivative instrument that has different types of underlying assets, such as a total return swap.
  """
  FLOATING_RATE_RETURN = "FLOATING_RATE_RETURN"
  """
  A cash flow corresponding to the return of the floating interest rate portion of a derivative instrument that has different types of underlying assets, such as a total return swap.
  """
  FRACTIONAL_AMOUNT = "FRACTIONAL_AMOUNT"
  """
  A cash flow corresponding to the compensation for missing assets due to the rounding of digits in the original number of assets to be delivered as per payout calculation.
  """
  INTEREST_RETURN = "INTEREST_RETURN"
  """
  A cash flow corresponding to the return of the interest rate portion of a derivative instrument that has different types of underlying assets, such as a total return swap.
  """
  NET_INTEREST = "NET_INTEREST"
  """
  Net interest across payout components. Applicable to products such as interest rate swaps.
  """
  PERFORMANCE = "PERFORMANCE"
  """
  A cash flow corresponding to a performance return.  The settlementOrigin attribute on the Transfer should point to the relevant Payout defining the performance calculation.
  """
  PRINCIPAL_PAYMENT = "PRINCIPAL_PAYMENT"
  """
  A cashflow which amount typically corresponds to the notional amount of the contract for various business reasons e.g. PhysicalSettlement, PrincipalExchange etc. else to a portion of the notional amount interim payments e.g. for the purpose of resetting the Notional Amount of a Cross Currency Swap variying leg, as part of a final Principal Exchange related to a Non-Deliverable currency leg, etc.
  """
