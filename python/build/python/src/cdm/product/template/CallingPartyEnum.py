from enum import Enum

all = ['CallingPartyEnum']
  
class CallingPartyEnum(Enum):
  """
  Identifies a party to the on-demand repo transaction that has a right to demand for termination of the Security Finance transaction.
  """
  AS_DEFINED_IN_MASTER_AGREEMENT = "AS_DEFINED_IN_MASTER_AGREEMENT"
  """
  As defined in Master Agreement.
  """
  EITHER = "EITHER"
  """
  Either, Buyer or Seller to the repo transaction.
  """
  INITIAL_BUYER = "INITIAL_BUYER"
  """
  Initial buyer to the repo transaction.
  """
  INITIAL_SELLER = "INITIAL_SELLER"
  """
  Initial seller to the repo transaction.
  """
