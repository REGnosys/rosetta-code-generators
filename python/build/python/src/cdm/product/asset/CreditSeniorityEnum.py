from enum import Enum

all = ['CreditSeniorityEnum']
  
class CreditSeniorityEnum(Enum):
  """
  Seniority of debt instruments comprising the index.
  """
  OTHER = "OTHER"
  """
  Other as defined under EMIR.
  """
  SENIOR_LOSS_ABSORBING_CAPACITY = "SENIOR_LOSS_ABSORBING_CAPACITY"
  """
  Senior Loss Absorbing Capacity (RED Tier Code: SNRLAC).
  """
  SENIOR_SEC = "SENIOR_SEC"
  """
  Senior domestic (RED Tier Code: SECDOM).
  """
  SENIOR_UN_SEC = "SENIOR_UN_SEC"
  """
  Senior foreign (RED Tier Code: SNRFOR).
  """
  SUB_LOWER_TIER_2 = "SUB_LOWER_TIER_2"
  """
  Subordinate, Lower Tier 2 (RED Tier Code: SUBLT2).
  """
  SUB_TIER_1 = "SUB_TIER_1"
  """
  Subordinate Tier 1 (RED Tier Code: PREFT1).
  """
  SUB_TIER_3 = "SUB_TIER_3"
  """
  Subordinate, Tier 3.
  """
  SUB_UPPER_TIER_2 = "SUB_UPPER_TIER_2"
  """
  Subordinate, Upper Tier 2 (RED Tier Code: JRSUBUT2).
  """
