from enum import Enum

all = ['RecalculationOfValueElectionEnum']
  
class RecalculationOfValueElectionEnum(Enum):
  """
  The enumerated values to specify the procedure under which the market value of posted collateral will be recalculated.
  """
  CONSULATION_PROCEDURE = "CONSULATION_PROCEDURE"
  """
  The parties agree to consult
  """
  NOT_APPLICABLE = "NOT_APPLICABLE"
  """
  Description to be added
  """
  OTHER_REGULATORY_CSA_PROCEDURE = "OTHER_REGULATORY_CSA_PROCEDURE"
  """
  The procedures specified in an Other Regulatory CSA
  """
  SPECIFIED = "SPECIFIED"
  """
  Bespoke Recalculation of value terms are specified in the agreement.
  """
