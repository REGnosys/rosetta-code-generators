from enum import Enum

all = ['DividendCompositionEnum']
  
class DividendCompositionEnum(Enum):
  """
  The enumerated values to specify how the composition of Dividends is to be determined.
  """
  CALCULATION_AGENT_ELECTION = "CALCULATION_AGENT_ELECTION"
  """
  The Calculation Agent determines the composition of dividends (subject to conditions).
  """
  EQUITY_AMOUNT_RECEIVER_ELECTION = "EQUITY_AMOUNT_RECEIVER_ELECTION"
  """
  The Equity Amount Receiver determines the composition of dividends (subject to conditions).
  """
