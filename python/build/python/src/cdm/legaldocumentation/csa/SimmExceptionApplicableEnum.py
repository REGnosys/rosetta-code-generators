from enum import Enum

all = ['SimmExceptionApplicableEnum']
  
class SimmExceptionApplicableEnum(Enum):
  """
  The enumerated values to the specify the SIMM normalized exception approaches applicable to the ISDA 2018 Standard CSA. ISDA 2018 Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  FALL_BACK_TO_MANDATORY_METHOD = "FALL_BACK_TO_MANDATORY_METHOD"
  """
  The ISDA Standard Initial Margin Model exception is applicable as a Fallback to Mandatory Method. ISDA 2018 Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  MANDATORY_METHOD = "MANDATORY_METHOD"
  """
  The ISDA Standard Initial Margin Model exception is applicable as a Mandatory Method. This means that the method applicable is to determine the Margin Amount (IM) by reference to the methodology prescribed pursuant to the applicable regulatory regime which uses a standardized initial margin schedule (such that prescribed percentages are applied to notional amounts before being adjusted, including by a net-to-gross ratio (NGR)). ISDA 2018 Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  OTHER_METHOD = "OTHER_METHOD"
  """
  An alternative approach is described in the document as follows.
  """
