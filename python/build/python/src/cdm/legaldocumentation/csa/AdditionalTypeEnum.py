from enum import Enum

all = ['AdditionalTypeEnum']
  
class AdditionalTypeEnum(Enum):
  """
  The enumerated values to specify the Additional Type of transaction that can require the collection or delivery of initial margin under a given regulatory regime for the purposes of Covered Transactions, as specified in ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (b)(B).
  """
  EQUITY_OPTION_OR_INDEX_OPTION = "EQUITY_OPTION_OR_INDEX_OPTION"
  """
  Single stock equity option or index option transaction as referred to in the transitional provisions (if any) of the EMIR RTS.
  """
  NOT_APPLICABLE = "NOT_APPLICABLE"
  """
  No Additional Type of transaction is applicable to the regulatory regulatory regime.
  """
  OTHER = "OTHER"
