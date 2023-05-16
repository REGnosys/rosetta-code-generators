from enum import Enum

all = ['ObligationCategoryEnum']
  
class ObligationCategoryEnum(Enum):
  """
  The enumerated values used in both the obligations and deliverable obligations of the credit default swap to represent a class or type of securities which apply.
  """
  BOND = "BOND"
  """
  ISDA term 'Bond'.
  """
  BOND_OR_LOAN = "BOND_OR_LOAN"
  """
  ISDA term 'Bond or Loan'.
  """
  BORROWED_MONEY = "BORROWED_MONEY"
  """
  ISDA term 'Borrowed Money'.
  """
  LOAN = "LOAN"
  """
  ISDA term 'Loan'.
  """
  PAYMENT = "PAYMENT"
  """
  ISDA term 'Payment'.
  """
  REFERENCE_OBLIGATIONS_ONLY = "REFERENCE_OBLIGATIONS_ONLY"
  """
  ISDA term 'Reference Obligations Only'.
  """
