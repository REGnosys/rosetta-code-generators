from enum import Enum

all = ['PayerReceiverEnum']
  
class PayerReceiverEnum(Enum):
  """
  The enumerated values to specify an interest rate stream payer or receiver party.
  """
  PAYER = "PAYER"
  """
  The party identified as the stream payer.
  """
  RECEIVER = "RECEIVER"
  """
  The party identified as the stream receiver.
  """
