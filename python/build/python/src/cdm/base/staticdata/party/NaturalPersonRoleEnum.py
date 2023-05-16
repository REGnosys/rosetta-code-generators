from enum import Enum

all = ['NaturalPersonRoleEnum']
  
class NaturalPersonRoleEnum(Enum):
  """
  The enumerated values for the natural person's role.
  """
  BROKER = "BROKER"
  """
  The person who arranged with a client to execute the trade.
  """
  BUYER = "BUYER"
  """
  Acquirer of the legal title to the financial instrument.
  """
  DECISION_MAKER = "DECISION_MAKER"
  """
  The party or person with legal responsibility for authorization of the execution of the transaction.
  """
  EXECUTION_WITHIN_FIRM = "EXECUTION_WITHIN_FIRM"
  """
  Person within the firm who is responsible for execution of the transaction.
  """
  INVESTMENT_DECISION_MAKER = "INVESTMENT_DECISION_MAKER"
  """
  Person who is responsible for making the investment decision.
  """
  SELLER = "SELLER"
  """
  Seller of the legal title to the financial instrument.
  """
  TRADER = "TRADER"
  """
  The person who executed the trade.
  """
