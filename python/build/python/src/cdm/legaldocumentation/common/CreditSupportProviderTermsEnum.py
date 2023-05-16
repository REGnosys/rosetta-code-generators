from enum import Enum

all = ['CreditSupportProviderTermsEnum']
  
class CreditSupportProviderTermsEnum(Enum):
  """
  The enumerated values to specify the Credit Support Provider Terms
  """
  ANY = "ANY"
  """
  Any party or parties who now or in the future may provide a Credit Support Document or other form of credit support.
  """
  NONE = "NONE"
  """
  No Credit Support Provider is specified.
  """
  SPECIFIED = "SPECIFIED"
  """
  A specified Credit Support Provider is provided
  """
