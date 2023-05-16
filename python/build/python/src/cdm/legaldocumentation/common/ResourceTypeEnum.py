from enum import Enum

all = ['ResourceTypeEnum']
  
class ResourceTypeEnum(Enum):
  """
  The enumerated values to specify the type of a resource (e.g. document).
  """
  CONFIRMATION = "CONFIRMATION"
  """
  Document describing the legal terms of a transaction.
  """
  SUPPLEMENTAL_MATERIAL_ECONOMIC_TERMS = "SUPPLEMENTAL_MATERIAL_ECONOMIC_TERMS"
  """
  Document providing supplemental material economic terms to the FpML data representation. The initial intended usage is to fulfill the CFTC Part 45 rule requirement to report ‘Any other terms(s) of the swap matched or affirmed by the counterparties in verifying the swap’ when the reporting is done via the generic FpML representation.
  """
  TERM_SHEET = "TERM_SHEET"
  """
  Document describing the economic characteristics of a transaction.
  """
