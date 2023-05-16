from enum import Enum

all = ['TransferStatusEnum']
  
class TransferStatusEnum(Enum):
  """
  The enumeration values to specify the transfer status.
  """
  DISPUTED = "DISPUTED"
  """
  The transfer is disputed.
  """
  INSTRUCTED = "INSTRUCTED"
  """
  The transfer has been instructed.
  """
  NETTED = "NETTED"
  """
  The transfer has been netted into a separate Transfer.
  """
  PENDING = "PENDING"
  """
  The transfer is pending instruction.
  """
  SETTLED = "SETTLED"
  """
  The transfer has been settled.
  """
