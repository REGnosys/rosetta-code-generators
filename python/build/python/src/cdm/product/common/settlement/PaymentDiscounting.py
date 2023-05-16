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

__all__ = ['PaymentDiscounting']


class PaymentDiscounting(BaseDataClass):
  """
  This class corresponds to the FpML PaymentDiscounting.model group for representing the discounting elements that can be associated with a payment.
  """
  discountFactor: Optional[Decimal] = Field(None, description="The value representing the discount factor used to calculate the present value of the cash flow.")
  """
  The value representing the discount factor used to calculate the present value of the cash flow.
  """
  presentValueAmount: Optional[Money] = Field(None, description="The amount representing the present value of the forecast payment.")
  """
  The amount representing the present value of the forecast payment.
  """

from cdm.observable.asset.Money import Money

PaymentDiscounting.update_forward_refs()
