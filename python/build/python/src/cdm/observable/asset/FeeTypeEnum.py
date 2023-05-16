from enum import Enum

all = ['FeeTypeEnum']
  
class FeeTypeEnum(Enum):
  """
  The enumerated values to specify an event that has given rise to a fee.
  """
  ASSIGNMENT = "ASSIGNMENT"
  """
  A cash flow resulting from the assignment of a contract to a new counterparty.
  """
  BROKERAGE_COMMISSION = "BROKERAGE_COMMISSION"
  """
  The brokerage commission.
  """
  CORPORATE_ACTION = "CORPORATE_ACTION"
  """
  A cash flow associated with a corporate action
  """
  CREDIT_EVENT = "CREDIT_EVENT"
  """
  A cash flow associated with a credit event.
  """
  INCREASE = "INCREASE"
  """
  A cash flow associated with an increase lifecycle event.
  """
  NOVATION = "NOVATION"
  """
  The novation fee.
  """
  PARTIAL_TERMINATION = "PARTIAL_TERMINATION"
  """
  A cash flow associated with a partial termination lifecycle event.
  """
  PREMIUM = "PREMIUM"
  """
  Denotes the amount payable by the buyer to the seller for an option. The premium is paid on the specified premium payment date or on each premium payment date if specified.
  """
  RENEGOTIATION = "RENEGOTIATION"
  """
  A cash flow associated with a renegotiation lifecycle event.
  """
  TERMINATION = "TERMINATION"
  """
  A cash flow associated with a termination lifecycle event.
  """
  UPFRONT = "UPFRONT"
  """
  An upfront cashflow associated to the swap to adjust for a difference between the swap price and the current market price.
  """
