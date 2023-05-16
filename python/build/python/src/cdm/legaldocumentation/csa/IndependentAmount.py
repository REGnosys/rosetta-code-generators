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

__all__ = ['IndependentAmount']

from cdm.base.staticdata.party.PartyReferencePayerReceiver import PartyReferencePayerReceiver

class IndependentAmount(PartyReferencePayerReceiver):
  """
  A class specifying the Independent Amount as the combination of a payer/receiver, a payment amount, a payment date and an associated payment calculation rule.
  """
  paymentDetail: List[PaymentDetail] = Field([], description="An attribute that specifies a payment as the combination of a payment amount, a payment date and an associated payment calculation rule.")
  """
  An attribute that specifies a payment as the combination of a payment amount, a payment date and an associated payment calculation rule.
  """
  @rosetta_condition
  def cardinality_paymentDetail(self):
    return check_cardinality(self.paymentDetail, 1, None)
  

from cdm.product.common.settlement.PaymentDetail import PaymentDetail

IndependentAmount.update_forward_refs()
