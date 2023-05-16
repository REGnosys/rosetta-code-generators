from enum import Enum

all = ['CounterpartyRoleEnum']
  
class CounterpartyRoleEnum(Enum):
  """
  Defines the enumerated values to specify the two counterparties to the transaction.
  """
  PARTY_1 = "PARTY_1"
  PARTY_2 = "PARTY_2"
