from enum import Enum

all = ['MatrixTypeEnum']
  
class MatrixTypeEnum(Enum):
  """
  The enumerated values to specify the identification the form of applicable matrix.
  """
  CREDIT_DERIVATIVES_PHYSICAL_SETTLEMENT_MATRIX = "CREDIT_DERIVATIVES_PHYSICAL_SETTLEMENT_MATRIX"
  """
  The ISDA-published Credit Derivatives Physical Settlement Matrix.
  """
  EQUITY_DERIVATIVES_MATRIX = "EQUITY_DERIVATIVES_MATRIX"
  """
  The ISDA-published Equity Derivatives Matrix.
  """
  SETTLEMENT_MATRIX = "SETTLEMENT_MATRIX"
  """
  The ISDA-published 2000 ISDA Definitions Settlement Matrix for Early Terminations and Swaptions.
  """
