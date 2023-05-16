from enum import Enum

all = ['OptionTypeEnum']
  
class OptionTypeEnum(Enum):
  """
  The enumerated values to specify the type of the option. In FpML, OptionTypeEnum is a union with PutCallEnum, which specifies whether the option is a put or a call.
  """
  CALL = "CALL"
  """
  A call option gives the holder the right to buy the underlying asset by a certain date for a certain price.
  """
  PAYER = "PAYER"
  """
  A 'payer' option: If you buy a 'payer' option you have the right but not the obligation to enter into the underlying swap transaction as the 'fixed' rate/price payer and receive float.
  """
  PUT = "PUT"
  """
  A put option gives the holder the right to sell the underlying asset by a certain date for a certain price.
  """
  RECEIVER = "RECEIVER"
  """
  A 'receiver' option: If you buy a 'receiver' option you have the right but not the obligation to enter into the underlying swap transaction as the 'fixed' rate/price receiver and pay float.
  """
  STRADDLE = "STRADDLE"
  """
  A straddle strategy, which involves the simultaneous buying of a put and a call of the same underlier, at the same strike and same expiration date
  """
