from enum import Enum

all = ['PositionStatusEnum']
  
class PositionStatusEnum(Enum):
  """
  Enumeration to describe the different (risk) states of a Position, whether executed, settled, matured...etc
  """
  CANCELLED = "CANCELLED"
  """
  The position has been cancelled, in case of a cancellation event following an execution.
  """
  CLOSED = "CLOSED"
  """
  The position has been closed, in case of a termination event.
  """
  EXECUTED = "EXECUTED"
  """
  The position has been executed, which is the point at which risk has been transferred.
  """
  FORMED = "FORMED"
  """
  Contract has been formed, in case position is on a contractual product.
  """
  SETTLED = "SETTLED"
  """
  The position has settled, in case product is subject to settlement after execution, such as securities.
  """
