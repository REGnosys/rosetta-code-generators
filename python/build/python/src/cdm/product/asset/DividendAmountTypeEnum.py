from enum import Enum

all = ['DividendAmountTypeEnum']
  
class DividendAmountTypeEnum(Enum):
  """
  The enumerated values to specify whether the dividend is paid with respect to the Dividend Period.
  """
  AS_SPECIFIED_IN_MASTER_CONFIRMATION = "AS_SPECIFIED_IN_MASTER_CONFIRMATION"
  """
  The Amount is determined as provided in the relevant Master Confirmation.
  """
  EX_AMOUNT = "EX_AMOUNT"
  """
  The ex-date for a dividend occurs during a dividend period.
  """
  PAID_AMOUNT = "PAID_AMOUNT"
  """
  The payment date for a dividend occurs during a dividend period.
  """
  RECORD_AMOUNT = "RECORD_AMOUNT"
  """
  The record date for a dividend occurs during a dividend period.
  """
