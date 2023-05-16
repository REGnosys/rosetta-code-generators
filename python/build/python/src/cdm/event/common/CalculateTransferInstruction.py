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

__all__ = ['CalculateTransferInstruction']


class CalculateTransferInstruction(BaseDataClass):
  """
  Defines the tradeState or payout on which to create a Transfer along with all necessary resets.
  """
  date: Optional[date] = Field(None, description="")
  payerReceiver: Optional[PayerReceiver] = Field(None, description="")
  payout: AttributeWithReference | Payout = Field(..., description="")
  quantity: Optional[Quantity] = Field(None, description="Specifies quantity amount returned if not the full amount from the TradeState, e.g. partial return")
  """
  Specifies quantity amount returned if not the full amount from the TradeState, e.g. partial return
  """
  resets: List[Reset] = Field([], description="")
  tradeState: TradeState = Field(..., description="")

from cdm.base.staticdata.party.PayerReceiver import PayerReceiver
from cdm.product.template.Payout import Payout
from cdm.base.math.Quantity import Quantity
from cdm.event.common.Reset import Reset
from cdm.event.common.TradeState import TradeState

CalculateTransferInstruction.update_forward_refs()
