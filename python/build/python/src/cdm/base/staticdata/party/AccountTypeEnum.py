from enum import Enum

all = ['AccountTypeEnum']
  
class AccountTypeEnum(Enum):
  """
  The enumeration values to qualify the type of account.
  """
  AGGREGATE_CLIENT = "AGGREGATE_CLIENT"
  """
  Aggregate client account, as defined under ESMA MiFIR.
  """
  CLIENT = "CLIENT"
  """
  The account contains trading activity or positions that belong to a client of the firm that opened the account.
  """
  HOUSE = "HOUSE"
  """
  The account contains proprietary trading activity or positions, belonging to the firm that is the owner of the account.
  """
