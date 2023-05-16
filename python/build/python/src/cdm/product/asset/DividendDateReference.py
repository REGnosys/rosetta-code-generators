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

__all__ = ['DividendDateReference']


class DividendDateReference(BaseDataClass):
  """
  A class to specify the dividend date by reference to another date, with the ability to apply and offset. This class doesn't exist in FpML and is meant to simplify the choice constraint associated with the DividendPaymentDate class.
  """
  dateReference: DividendDateReferenceEnum = Field(..., description="Specification of the dividend date using an enumeration, with values such as the pay date, the ex-date or the record date.")
  """
  Specification of the dividend date using an enumeration, with values such as the pay date, the ex-date or the record date.
  """
  paymentDateOffset: Optional[Offset] = Field(None, description="Only to be used when SharePayment has been specified in the dividendDateReference element. The number of Currency Business Days following the day on which the Issuer of the Shares pays the relevant dividend to holders of record of the Shares.")
  """
  Only to be used when SharePayment has been specified in the dividendDateReference element. The number of Currency Business Days following the day on which the Issuer of the Shares pays the relevant dividend to holders of record of the Shares.
  """
  
  @rosetta_condition
  def condition_0_PaymentDateOffset(self):
    """
     FpML specifies that paymentDateOffset is only to be used when SharePayment has been specified in the dividendDateReference element.
    """
    def _then_fn0():
      return all_elements(self.dateReference, "=", DividendDateReferenceEnum.SHARE_PAYMENT)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.paymentDateOffset) is not None), _then_fn0, _else_fn0)

from cdm.product.asset.DividendDateReferenceEnum import DividendDateReferenceEnum
from cdm.base.datetime.Offset import Offset

DividendDateReference.update_forward_refs()
