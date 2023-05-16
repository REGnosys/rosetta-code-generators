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

__all__ = ['FeaturePayment']


class FeaturePayment(BaseDataClass):
  """
  Payment made following trigger occurrence.
  """
  amount: Optional[Decimal] = Field(None, description="The monetary quantity in currency units.")
  """
  The monetary quantity in currency units.
  """
  currency: Optional[AttributeWithMeta[str] | str] = Field(None, description="The currency in which an amount is denominated.")
  """
  The currency in which an amount is denominated.
  """
  levelPercentage: Optional[Decimal] = Field(None, description="The trigger level percentage.")
  """
  The trigger level percentage.
  """
  payerReceiver: PartyReferencePayerReceiver = Field(..., description="This attribute doesn't exist as part of the FpML construct, which makes use of the PayerReceiver.model group.")
  """
  This attribute doesn't exist as part of the FpML construct, which makes use of the PayerReceiver.model group.
  """
  paymentDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The feature payment date.")
  """
  The feature payment date.
  """
  time: Optional[TimeTypeEnum] = Field(None, description="The feature payment time.")
  """
  The feature payment time.
  """
  
  @rosetta_condition
  def condition_0_FeaturePaymentChoice(self):
    """
     Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('levelPercentage', 'amount', necessity=True)
  
  @rosetta_condition
  def condition_1_Amount(self):
    """
     The amount attribute is specified in FpML as non-negative decimal.
    """
    def _then_fn0():
      return all_elements(self.amount, ">=", 0.0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.amount) is not None), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.PartyReferencePayerReceiver import PartyReferencePayerReceiver
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.observable.common.TimeTypeEnum import TimeTypeEnum

FeaturePayment.update_forward_refs()
