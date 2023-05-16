from enum import Enum

all = ['MarginCallResponseTypeEnum']
  
class MarginCallResponseTypeEnum(Enum):
  """
  Represents the enumeration values to define the response type to a margin call.
  """
  AGREEIN_FULL = "AGREEIN_FULL"
  """
  Specifies a 'Full Agreement' to Margin Call.
  """
  DISPUTE = "DISPUTE"
  """
  Specifies a 'Full Dispute' to a Margin call.
  """
  PARTIALLY_AGREE = "PARTIALLY_AGREE"
  """
  Specifies a 'Partial agreement' to Margin Call.
  """
