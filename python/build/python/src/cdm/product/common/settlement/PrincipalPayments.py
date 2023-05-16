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

__all__ = ['PrincipalPayments']


class PrincipalPayments(BaseDataClass):
  """
  A class defining which principal exchanges occur for the stream.
  """
  finalPayment: bool = Field(..., description="A true/false flag to indicate whether there is a final exchange of principal on the termination date.")
  """
  A true/false flag to indicate whether there is a final exchange of principal on the termination date.
  """
  initialPayment: bool = Field(..., description="A true/false flag to indicate whether there is an initial exchange of principal on the effective date.")
  """
  A true/false flag to indicate whether there is an initial exchange of principal on the effective date.
  """
  intermediatePayment: bool = Field(..., description="A true/false flag to indicate whether there are intermediate or interim exchanges of principal during the term of the swap.")
  """
  A true/false flag to indicate whether there are intermediate or interim exchanges of principal during the term of the swap.
  """
  principalPaymentSchedule: Optional[PrincipalPaymentSchedule] = Field(None, description="Describe dates schedules for Principal Exchanges and related role of the parties when known.")
  """
  Describe dates schedules for Principal Exchanges and related role of the parties when known.
  """
  varyingLegNotionalCurrency: List[str] = Field([], description="Indicate the Payout legs which nominal amount may vary in regards of FX Fixing dates as determined in the product terms.")
  """
  Indicate the Payout legs which nominal amount may vary in regards of FX Fixing dates as determined in the product terms.
  """

from cdm.product.common.settlement.PrincipalPaymentSchedule import PrincipalPaymentSchedule

PrincipalPayments.update_forward_refs()
