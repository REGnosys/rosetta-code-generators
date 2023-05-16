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

__all__ = ['BillingRecord']


class BillingRecord(BaseDataClass):
  """
  Specifies individual records within a billing invoice.
  """
  minimumFee: Optional[Money] = Field(None, description="Indicates the minimum fee amount applied to the billing record, if any.")
  """
  Indicates the minimum fee amount applied to the billing record, if any.
  """
  recordEndDate: date = Field(..., description="The ending date of the period described by this record")
  """
  The ending date of the period described by this record
  """
  recordStartDate: date = Field(..., description="The starting date of the period described by this record")
  """
  The starting date of the period described by this record
  """
  recordTransfer: Transfer = Field(..., description="The settlement terms for the billing record")
  """
  The settlement terms for the billing record
  """
  tradeState: AttributeWithReference | TradeState = Field(..., description="The trade for the individual billing record.")
  """
  The trade for the individual billing record.
  """

from cdm.observable.asset.Money import Money
from cdm.event.common.Transfer import Transfer
from cdm.event.common.TradeState import TradeState

BillingRecord.update_forward_refs()
