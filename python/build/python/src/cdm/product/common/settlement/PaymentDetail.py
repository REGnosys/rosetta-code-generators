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

__all__ = ['PaymentDetail']


class PaymentDetail(BaseDataClass):
  paymentAmount: Optional[Money] = Field(None, description="A fixed payment amount.")
  """
  A fixed payment amount.
  """
  paymentDate: Optional[AdjustableOrRelativeDate] = Field(None, description="")
  paymentRule: PaymentRule = Field(..., description="The calculation rule.")
  """
  The calculation rule.
  """

from cdm.observable.asset.Money import Money
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.product.common.settlement.PaymentRule import PaymentRule

PaymentDetail.update_forward_refs()
