from enum import Enum

all = ['TerminationCurrencyConditionEnum']
  
class TerminationCurrencyConditionEnum(Enum):
  FREELY_AVAILABLE = "FREELY_AVAILABLE"
  """
  A currency that is freely available.
  """
  PAYMENTS_DUE = "PAYMENTS_DUE"
  """
  A currency in which payments would be due under one or more Transactions.
  """
  PAYMENTS_DUE_AND_FREELY_AVAILABLE = "PAYMENTS_DUE_AND_FREELY_AVAILABLE"
  """
  A currency in which payments would be due under one or more Transactions and that is freely available.
  """
  SPECIFIED = "SPECIFIED"
  """
  Termination Currency Conditions are specified.
  """
