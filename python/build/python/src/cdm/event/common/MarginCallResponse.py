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

__all__ = ['MarginCallResponse']

from cdm.event.common.MarginCallBase import MarginCallBase

class MarginCallResponse(MarginCallBase):
  """
  Represents common attributes required for a Margin Call Response under a legal agreement such as a credit support document or equivalent.
  """
  agreedAmountBaseCurrency: Money = Field(..., description="Indicates the amount that posting entity agrees to remit in response to margin call (in base currency).")
  """
  Indicates the amount that posting entity agrees to remit in response to margin call (in base currency).
  """
  marginCallResponseAction: List[MarginCallResponseAction] = Field([], description="Specifies the margin call action details, including collateral to be moved and direction.")
  """
  Specifies the margin call action details, including collateral to be moved and direction.
  """
  @rosetta_condition
  def cardinality_marginCallResponseAction(self):
    return check_cardinality(self.marginCallResponseAction, 1, None)
  
  marginResponseType: MarginCallResponseTypeEnum = Field(..., description="Indicates the response type, such as, is the margin call response a 'full' 'part' agreement or 'dispute'.")
  """
  Indicates the response type, such as, is the margin call response a 'full' 'part' agreement or 'dispute'.
  """

from cdm.observable.asset.Money import Money
from cdm.event.common.MarginCallResponseAction import MarginCallResponseAction
from cdm.event.common.MarginCallResponseTypeEnum import MarginCallResponseTypeEnum

MarginCallResponse.update_forward_refs()
