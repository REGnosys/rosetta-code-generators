from enum import Enum

all = ['PartyDeterminationEnum']
  
class PartyDeterminationEnum(Enum):
  """
  The enumerated values to specify how a calculation agent will be determined.
  """
  AS_SPECIFIED_IN_MASTER_AGREEMENT = "AS_SPECIFIED_IN_MASTER_AGREEMENT"
  """
  The Calculation Agent is determined by reference to the relevant master agreement.
  """
  AS_SPECIFIED_IN_STANDARD_TERMS_SUPPLEMENT = "AS_SPECIFIED_IN_STANDARD_TERMS_SUPPLEMENT"
  """
  The Calculation Agent is determined by reference to the relevant standard terms supplement.
  """
  BOTH = "BOTH"
  """
  Both parties with joined rights to be a calculation agent.
  """
  EXERCISING_PARTY = "EXERCISING_PARTY"
  """
  The party that gives notice of exercise. Per 2000 ISDA Definitions, Section 11.1. Parties, paragraph (d).
  """
  NON_EXERCISING_PARTY = "NON_EXERCISING_PARTY"
  """
  The party that is given notice of exercise. Per 2000 ISDA Definitions, Section 11.1. Parties, paragraph (e).
  """
