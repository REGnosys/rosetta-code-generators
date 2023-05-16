from enum import Enum

all = ['TransferSettlementEnum']
  
class TransferSettlementEnum(Enum):
  """
  The enumeration values to specify how the transfer will settle, e.g. DvP.
  """
  DELIVERY_VERSUS_DELIVERY = "DELIVERY_VERSUS_DELIVERY"
  """
  Simultaneous transfer of two assets, typically securities, as a way to avoid settlement risk.
  """
  DELIVERY_VERSUS_PAYMENT = "DELIVERY_VERSUS_PAYMENT"
  """
  Settlement in which the transfer of the asset and the cash settlement are simultaneous.
  """
  NOT_CENTRAL_SETTLEMENT = "NOT_CENTRAL_SETTLEMENT"
  """
  No central settlement.
  """
  PAYMENT_VERSUS_PAYMENT = "PAYMENT_VERSUS_PAYMENT"
  """
  Simultaneous transfer of cashflows.
  """
