from enum import Enum

all = ['MortgageSectorEnum']
  
class MortgageSectorEnum(Enum):
  """
  The enumerated values to specify a mortgage typology.
  """
  ABS = "ABS"
  """
  Asset Backed Security.
  """
  CDO = "CDO"
  """
  Collateralized Debt Obligation.
  """
  CMBS = "CMBS"
  """
  Commercial Mortgage Backed Security.
  """
  RMBS = "RMBS"
  """
  Residential Mortgage Backed Security.
  """
