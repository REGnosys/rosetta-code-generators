from enum import Enum

all = ['CreditSupportDocumentTermsEnum']
  
class CreditSupportDocumentTermsEnum(Enum):
  """
  The enumerated values to specify the Credit Support Document Terms
  """
  ANY = "ANY"
  """
  Any guarantee, collateral arrangement and/or other agreement or arrangement which provides for credit support with respect to the party’s obligations under this Agreement.
  """
  NONE = "NONE"
  """
  No Credit Support Document is specified.
  """
  SPECIFIED = "SPECIFIED"
  """
  A specified Credit Support Document is provided
  """
