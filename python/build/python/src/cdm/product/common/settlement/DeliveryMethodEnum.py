from enum import Enum

all = ['DeliveryMethodEnum']
  
class DeliveryMethodEnum(Enum):
  """
  Specifies delivery methods for securities transactions. This coding-scheme defines the possible delivery methods for securities.
  """
  DELIVERY_VERSUS_PAYMENT = "DELIVERY_VERSUS_PAYMENT"
  """
  Indicates that a securities delivery must be made against payment in simultaneous transmissions and stipulate each other.
  """
  FREE_OF_PAYMENT = "FREE_OF_PAYMENT"
  """
  Indicates that a securities delivery can be made without a simultaneous cash payment in exchange and not depending on if payment obligations are fulfilled or not and vice versa.
  """
  PRE_DELIVERY = "PRE_DELIVERY"
  """
  Indicates that a securities delivery must be made in full before the payment for the securities; fulfillment of payment obligations depends on securities delivery obligations fulfillment.
  """
  PRE_PAYMENT = "PRE_PAYMENT"
  """
  Indicates that a payment in full amount must be made before the securities delivery; fulfillment of securities delivery obligations depends on payment obligations fulfillment.
  """
