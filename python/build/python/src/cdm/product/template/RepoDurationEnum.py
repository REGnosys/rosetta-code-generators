from enum import Enum

all = ['RepoDurationEnum']
  
class RepoDurationEnum(Enum):
  """
  A duration code for a Repo (or Securities Lending) transaction. There are many business and market rules that are derived from the duration of the transaction.
  """
  OVERNIGHT = "OVERNIGHT"
  """
  Indicates that a contract is classified as overnight, meaning that there is one business day difference between the start and end date of the contract. Business rule: When the repo is overnight, the number of business days between the spot and forward value dates must be one. Forward leg must be specified.
  """
  TERM = "TERM"
  """
  Indicates that a contract is a regular term contract, with a start date and an end date. Business rule: When the repo is 'Term', both spot and forward legs must be specified.
  """
