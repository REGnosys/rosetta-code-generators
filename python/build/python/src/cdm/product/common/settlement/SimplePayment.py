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

__all__ = ['SimplePayment']

from cdm.base.staticdata.party.PartyReferencePayerReceiver import PartyReferencePayerReceiver

class SimplePayment(PartyReferencePayerReceiver):
  """
  A class to specified payments in a simpler fashion than the Payment type. This construct should be used from the FpML version 4.3 onwards.
  """
  paymentAmount: Money = Field(..., description="The payment amount.")
  """
  The payment amount.
  """
  paymentDate: AdjustableOrRelativeDate = Field(..., description="The payment date. This date is subject to adjustment in accordance with any applicable business day convention.")
  """
  The payment date. This date is subject to adjustment in accordance with any applicable business day convention.
  """
  
  @rosetta_condition
  def condition_0_NonNegativePaymentAmount(self):
    """
    FpML specifies paymentAmount as NonNegativeMoney.
    """
    return all_elements(self.paymentAmount.value, ">", 0.0)

from cdm.observable.asset.Money import Money
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate

SimplePayment.update_forward_refs()
