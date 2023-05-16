from enum import Enum

all = ['SettlementTypeEnum']
  
class SettlementTypeEnum(Enum):
  """
  The enumeration values to specify how the option is to be settled when exercised.
  """
  CASH = "CASH"
  """
  The intrinsic value of the option will be delivered by way of a cash settlement amount determined, (i) by reference to the differential between the strike price and the settlement price; or (ii) in accordance with a bilateral agreement between the parties.
  """
  CASH_OR_PHYSICAL = "CASH_OR_PHYSICAL"
  """
  Allow use of either Cash or Physical settlement without prior Election.
  """
  ELECTION = "ELECTION"
  """
  Allow Election of either Cash or Physical settlement.
  """
  PHYSICAL = "PHYSICAL"
  """
  The securities underlying the transaction will be delivered by (i) in the case of a call, the seller to the buyer, or (ii) in the case of a put, the buyer to the seller versus a settlement amount equivalent to the strike price per share.
  """
