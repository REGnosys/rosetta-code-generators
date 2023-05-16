from enum import Enum

all = ['IndexEventConsequenceEnum']
  
class IndexEventConsequenceEnum(Enum):
  """
  The enumerated values to specify the consequences of Index Events.
  """
  CALCULATION_AGENT_ADJUSTMENT = "CALCULATION_AGENT_ADJUSTMENT"
  """
  Calculation Agent Adjustment.
  """
  CANCELLATION_AND_PAYMENT = "CANCELLATION_AND_PAYMENT"
  """
  Cancellation and Payment.
  """
  NEGOTIATED_CLOSE_OUT = "NEGOTIATED_CLOSE_OUT"
  """
  Negotiated Close Out.
  """
  RELATED_EXCHANGE = "RELATED_EXCHANGE"
  """
  Related Exchange.
  """
