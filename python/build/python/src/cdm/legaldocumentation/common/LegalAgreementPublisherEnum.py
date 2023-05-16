from enum import Enum

all = ['LegalAgreementPublisherEnum']
  
class LegalAgreementPublisherEnum(Enum):
  """
  The enumerated values to specify the legal agreement publisher.
  """
  AFB = "AFB"
  """
  Association Française des Banques.
  """
  BNYM = "BNYM"
  """
  BNY Mellon
  """
  ISDA = "ISDA"
  """
  International Swaps and Derivatives Association, Inc.
  """
  ISDA_CLEARSTREAM = "ISDA_CLEARSTREAM"
  """
  ISDA and Clearstream
  """
  ISDA_EUROCLEAR = "ISDA_EUROCLEAR"
  """
  ISDA and Euroclear
  """
  ISLA = "ISLA"
  """
  International Securities Lending Association
  """
  JP_MORGAN = "JP_MORGAN"
  """
  JP Morgan
  """
