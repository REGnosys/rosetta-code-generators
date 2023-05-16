# pylint: disable=line-too-long, invalid-name, missing-function-docstring, missing-module-docstring, superfluous-parens
# pylint: disable=wrong-import-position, unused-import, unused-wildcard-import, wildcard-import, wrong-import-order, missing-class-docstring
from __future__ import annotations
from typing import List, Optional
from datetime import date
from datetime import time
from datetime import datetime
from decimal import Decimal
from pydantic import Field
from rosetta.runtime.utils import *

__all__ = ['BillingSummary']


class BillingSummary(BaseDataClass):
  """
  Specifies individual summaries within a billing invoice.
  """
  summaryAmountType: RecordAmountTypeEnum = Field(..., description="The account level for the billing summary.")
  """
  The account level for the billing summary.
  """
  summaryTransfer: Optional[Transfer] = Field(None, description="The settlement terms for the billing summary")
  """
  The settlement terms for the billing summary
  """
  
  @rosetta_condition
  def condition_0_GrandTotal(self):
    def _then_fn0():
      return (((self.summaryTransfer) is not None) and ((self.summaryTransfer.payerReceiver) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.summaryAmountType, "=", RecordAmountTypeEnum.GRAND_TOTAL), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_ParentTotal(self):
    def _then_fn0():
      return ((((self.summaryTransfer.payerReceiver) is not None) and ((self.summaryTransfer.payerReceiver.payerAccountReference) is None)) and ((self.summaryTransfer.payerReceiver.receiverAccountReference) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.summaryAmountType, "=", RecordAmountTypeEnum.PARENT_TOTAL), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_AccountTotal(self):
    def _then_fn0():
      return (((self.summaryTransfer.payerReceiver.payerAccountReference) is not None) and ((self.summaryTransfer.payerReceiver.receiverAccountReference) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.summaryAmountType, "=", RecordAmountTypeEnum.ACCOUNT_TOTAL), _then_fn0, _else_fn0)

from cdm.event.common.RecordAmountTypeEnum import RecordAmountTypeEnum
from cdm.event.common.Transfer import Transfer

BillingSummary.update_forward_refs()
