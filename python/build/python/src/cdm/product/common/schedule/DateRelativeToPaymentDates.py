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

__all__ = ['DateRelativeToPaymentDates']


class DateRelativeToPaymentDates(BaseDataClass):
  """
  A data to:  provide the ability to point to multiple payment nodes in the document through the unbounded paymentDatesReference.
  """
  paymentDatesReference: List[AttributeWithReference | PaymentDates] = Field([], description="A set of href pointers to payment dates defined somewhere else in the document.")
  """
  A set of href pointers to payment dates defined somewhere else in the document.
  """
  @rosetta_condition
  def cardinality_paymentDatesReference(self):
    return check_cardinality(self.paymentDatesReference, 1, None)
  

from cdm.product.common.schedule.PaymentDates import PaymentDates

DateRelativeToPaymentDates.update_forward_refs()
