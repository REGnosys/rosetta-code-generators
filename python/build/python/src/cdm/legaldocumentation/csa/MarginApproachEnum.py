from enum import Enum

all = ['MarginApproachEnum']
  
class MarginApproachEnum(Enum):
  """
  The enumerated values to specify the margin approach specific to Initial Margin agreements.
  """
  ALLOCATED = "ALLOCATED"
  """
  (B) If the 'Allocated Margin Flow (IM/IA) Approach' is specified as applicable in Paragraph 13, the following provisions will apply: (1) 'Credit Support Amount (IM)' means, with respect to a party as the Pledgor, for any Calculation Date (IM), (i) the Margin Amount (IM) applicable to the Pledgor, if any, minus (ii) the Pledgor’s Threshold (IM); provided, however, that the Credit Support Amount (IM) will be deemed to be zero whenever the calculation of the Credit Support Amount (IM) yields a number less than zero. (2) Amendment to Obligations in respect of Margin Amount (IA). The posting obligation of a Pledgor in respect of any amount that constitutes a Margin Amount (IA) under any Other CSA shall be reduced on an aggregate basis by the amount of the Pledgor’s Credit Support Amount (IM); provided, however, that if, after such reduction, any such Margin Amount (IA) would be a negative amount, such Margin Amount (IA) will be deemed to be zero.
  """
  DISTINCT = "DISTINCT"
  """
  (A) If the 'Distinct Margin Flow (IM) Approach' is specified as applicable in Paragraph 13, the following provisions will apply: (1) 'Credit Support Amount (IM)' means, with respect to a party as the Pledgor, for any Calculation Date (IM), (i) the Margin Amount (IM) applicable to the Pledgor, if any, minus (ii) the Pledgor’s Threshold (IM); provided, however, that the Credit Support Amount (IM) will be deemed to be zero whenever the calculation of the Credit Support Amount (IM) yields a number less than zero. (2) No Amendment to Obligations in respect of Margin Amount (IA). The posting obligation of a Pledgor in respect of any amount that constitutes a Margin Amount (IA) under any Other CSA shall not be affected or amended in any way by the provisions of this Annex.
  """
  GREATER_OF = "GREATER_OF"
  """
  (C) If the 'Greater of Margin Flow (IM/IA) Approach' is specified as applicable in Paragraph 13, the following provisions will apply: (1) 'Credit Support Amount (IM)' means, with respect to a party as the Pledgor, for any Calculation Date (IM), the greater of (i)(A) the Margin Amount (IM) applicable to the Pledgor, if any, minus (B) the Pledgor’s Threshold (IM) and (ii) the Margin Amount (IA); provided, however, that the Credit Support Amount (IM) will be deemed to be zero whenever the calculation of the Credit Support Amount (IM) yields a number less than zero. (2) Amendment to Obligations in respect of Margin Amount (IA).  The posting obligation of a Pledgor in respect of any amount that constitutes a Margin Amount (IA) under any Other CSA, other than such obligations of a Pledgor under this Annex, shall be reduced to zero.
  """
