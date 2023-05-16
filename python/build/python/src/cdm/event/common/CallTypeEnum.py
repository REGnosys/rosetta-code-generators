from enum import Enum

all = ['CallTypeEnum']
  
class CallTypeEnum(Enum):
  """
  Represents the enumeration values that indicate the intended status of message type, such as expected call, notification of a call or a margin call.
  """
  EXPECTED_CALL = "EXPECTED_CALL"
  """
  Identifies an expected Margin Call instruction for either party to notify the other or their service provider of an expected margin call movement.
  """
  MARGIN_CALL = "MARGIN_CALL"
  """
  Identifies an actionable Margin Call.
  """
  NOTIFICATION = "NOTIFICATION"
  """
  Identifies a notification of a Margin Call for legal obligation to notify other party to initiate a margin call when notifying party is calculation or valuation agent.
  """
