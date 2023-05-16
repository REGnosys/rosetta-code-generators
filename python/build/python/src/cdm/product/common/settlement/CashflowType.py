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

__all__ = ['CashflowType']


class CashflowType(BaseDataClass):
  """
  Characterises the type of cashflow, which can result from either a scheduled or a non-scheduled lifecycle event.
  """
  cashPrice: Optional[CashPrice] = Field(None, description="Type of cashflow corresponding to a non-scheduled event, where a price must be agreed between the parties.")
  """
  Type of cashflow corresponding to a non-scheduled event, where a price must be agreed between the parties.
  """
  cashflowType: Optional[ScheduledTransferEnum] = Field(None, description="Type of cashflow corresponding to a scheduled event.")
  """
  Type of cashflow corresponding to a scheduled event.
  """
  grossOrNet: Optional[GrossOrNetEnum] = Field(None, description="Whether the cashflow is gross, net or a commission, if any.")
  """
  Whether the cashflow is gross, net or a commission, if any.
  """
  priceExpression: Optional[PriceExpressionEnum] = Field(None, description="")
  
  @rosetta_condition
  def condition_0_(self):
    """
    A cashflow is either specified as a type of scheduled cashflow, or as a price agreed between parties in case of a non-scheduled cashflow.
    """
    return self.check_one_of_constraint('cashflowType', 'cashPrice', necessity=True)

from cdm.observable.asset.CashPrice import CashPrice
from cdm.product.common.settlement.ScheduledTransferEnum import ScheduledTransferEnum
from cdm.observable.asset.GrossOrNetEnum import GrossOrNetEnum
from cdm.observable.asset.PriceExpressionEnum import PriceExpressionEnum

CashflowType.update_forward_refs()
