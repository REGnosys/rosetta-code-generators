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

__all__ = ['ExerciseFeeSchedule']

from cdm.base.staticdata.party.PayerReceiver import PayerReceiver

class ExerciseFeeSchedule(PayerReceiver):
  """
  A class to define a fee or schedule of fees to be payable on the exercise of an option. This fee may be defined as an amount or a percentage of the notional exercised. As a difference with FpML, it extends the BuyerSeller class.
  """
  feeAmountSchedule: Optional[AmountSchedule] = Field(None, description="The exercise fee amount schedule. The fees are expressed as currency amounts. The currency of the fee is assumed to be that of the notional schedule referenced.")
  """
  The exercise fee amount schedule. The fees are expressed as currency amounts. The currency of the fee is assumed to be that of the notional schedule referenced.
  """
  feePaymentDate: RelativeDateOffset = Field(..., description="The date on which exercise fee(s) will be paid. It is specified as a relative date.")
  """
  The date on which exercise fee(s) will be paid. It is specified as a relative date.
  """
  feeRateSchedule: Optional[Schedule] = Field(None, description="The exercise free rate schedule. The fees are expressed as percentage rates of the notional being exercised. The currency of the fee is assumed to be that of the notional schedule referenced.")
  """
  The exercise free rate schedule. The fees are expressed as percentage rates of the notional being exercised. The currency of the fee is assumed to be that of the notional schedule referenced.
  """
  notionalReference: AttributeWithReference | Money = Field(..., description="A pointer style reference to the associated notional schedule defined elsewhere in the document.")
  """
  A pointer style reference to the associated notional schedule defined elsewhere in the document.
  """
  
  @rosetta_condition
  def condition_0_ExerciseFeeScheduleChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('feeAmountSchedule', 'feeRateSchedule', necessity=True)

from cdm.product.common.schedule.AmountSchedule import AmountSchedule
from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset
from cdm.base.math.Schedule import Schedule
from cdm.observable.asset.Money import Money

ExerciseFeeSchedule.update_forward_refs()
