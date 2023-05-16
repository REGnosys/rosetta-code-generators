from enum import Enum

all = ['SensitivitiesEnum']
  
class SensitivitiesEnum(Enum):
  """
  The enumerated values to specify the methodology according to which sensitivities to (i) equity indices, funds and ETFs, and (ii) commodity indices are computed. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (gg)(2).
  """
  ALTERNATIVE = "ALTERNATIVE"
  """
  The parties agree that in respect of the relevant sensitivities, the delta is allocated back to individual constituents.
  """
  STANDARD = "STANDARD"
  """
  The relevant sensitivities are addressed by the standard preferred approach where the entire delta is put into the applicable asset class/category.
  """
