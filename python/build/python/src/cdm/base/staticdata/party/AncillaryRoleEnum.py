from enum import Enum

all = ['AncillaryRoleEnum']
  
class AncillaryRoleEnum(Enum):
  """
  Defines the enumerated values to specify the ancillary roles to the transaction. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and the AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference.
  """
  CALCULATION_AGENT_FALLBACK = "CALCULATION_AGENT_FALLBACK"
  """
  Specifies the party responsible for deciding the fallback rate.
  """
  CALCULATION_AGENT_INDEPENDENT = "CALCULATION_AGENT_INDEPENDENT"
  """
  Specifies the party responsible for performing calculation agent duties as defined in the applicable product definition.
  """
  CALCULATION_AGENT_MANDATORY_EARLY_TERMINATION = "CALCULATION_AGENT_MANDATORY_EARLY_TERMINATION"
  """
  Specifies the party responsible for performing calculation agent duties associated with an mandatory early termination.
  """
  CALCULATION_AGENT_OPTIONAL_EARLY_TERMINATION = "CALCULATION_AGENT_OPTIONAL_EARLY_TERMINATION"
  """
  Specifies the party responsible for performing calculation agent duties associated with an optional early termination.
  """
  DISRUPTION_EVENTS_DETERMINING_PARTY = "DISRUPTION_EVENTS_DETERMINING_PARTY"
  """
  Specifies the party which determines additional disruption events.
  """
  EXERCISE_NOTICE_RECEIVER_PARTY_CANCELABLE_PROVISION = "EXERCISE_NOTICE_RECEIVER_PARTY_CANCELABLE_PROVISION"
  """
  Specifies the party to which notice of a cancelable provision exercise should be given.
  """
  EXERCISE_NOTICE_RECEIVER_PARTY_EXTENDIBLE_PROVISION = "EXERCISE_NOTICE_RECEIVER_PARTY_EXTENDIBLE_PROVISION"
  """
  Specifies the party to which notice of a extendible provision exercise should be given.
  """
  EXERCISE_NOTICE_RECEIVER_PARTY_MANUAL = "EXERCISE_NOTICE_RECEIVER_PARTY_MANUAL"
  """
  Specifies the party to which notice of a manual exercise should be given.
  """
  EXERCISE_NOTICE_RECEIVER_PARTY_OPTIONAL_EARLY_TERMINATION = "EXERCISE_NOTICE_RECEIVER_PARTY_OPTIONAL_EARLY_TERMINATION"
  """
  Specifies the party to which notice of a optional early termination exercise should be given.
  """
  EXTRAORDINARY_DIVIDENDS_PARTY = "EXTRAORDINARY_DIVIDENDS_PARTY"
  """
  Specifies the party which determines if dividends are extraordinary in relation to normal levels.
  """
  PREDETERMINED_CLEARING_ORGANIZATION_PARTY = "PREDETERMINED_CLEARING_ORGANIZATION_PARTY"
  """
  Specifies the clearing organization (CCP, DCO) which the trade should be cleared.
  """
