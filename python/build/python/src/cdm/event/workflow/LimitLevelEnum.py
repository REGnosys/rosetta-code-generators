from enum import Enum

all = ['LimitLevelEnum']
  
class LimitLevelEnum(Enum):
  """
  The enumeration values to specify the level at which the limit is set: customer business, proprietary business or account level. This is part of the CME specification for clearing credit limits, although not specified as a set of enumerated values as part of the clearing confirmation specification.
  """
  ACCOUNT = "ACCOUNT"
  """
  The limit is set in relation to the proprietary business undertaken by the clearing counterparty.
  """
  CUSTOMER = "CUSTOMER"
  """
  The limit is set in relation to the customer business undertaken by the clearing counterparty.
  """
  HOUSE = "HOUSE"
  """
  The limit is set at the account level in relation to the clearing counterparty.
  """
