from enum import Enum

all = ['AmendmentEffectiveDateEnum']
  
class AmendmentEffectiveDateEnum(Enum):
  """
  The enumerated values to specify the effective date of the Amendment to Termination Currency when specified as a specific date (e.g. the annex date). ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (t).
  """
  AGREEMENT_DATE = "AGREEMENT_DATE"
  """
  The effective date corresponds to the Agreement date.
  """
  AMENDMENT_EFFECTIVE_DATE = "AMENDMENT_EFFECTIVE_DATE"
  """
  The effective date corresponds to the Amendment Effective Date (IM)
  """
  ANNEX_DATE = "ANNEX_DATE"
  """
  The effective date corresponds to the Annex date.
  """
  DEED_DATE = "DEED_DATE"
  """
  The effective date corresponds to the Deed date.
  """
