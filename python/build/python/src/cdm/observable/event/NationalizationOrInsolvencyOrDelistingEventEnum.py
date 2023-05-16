from enum import Enum

all = ['NationalizationOrInsolvencyOrDelistingEventEnum']
  
class NationalizationOrInsolvencyOrDelistingEventEnum(Enum):
  """
  Defines the consequences of nationalization, insolvency and delisting events relating to the underlying.
  """
  CANCELLATION_AND_PAYMENT = "CANCELLATION_AND_PAYMENT"
  """
  The trade is terminated.
  """
  NEGOTIATED_CLOSEOUT = "NEGOTIATED_CLOSEOUT"
  """
  The parties may, but are not obliged, to terminate the transaction on mutually acceptable terms and if the terms are not agreed then the transaction continues.
  """
