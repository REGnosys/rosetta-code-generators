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

__all__ = ['Transfer']

from cdm.event.common.TransferBase import TransferBase

class Transfer(TransferBase):
  """
  Defines the movement of cash, securities or commodities between two parties on a date.
  """
  resetOrigin: Optional[Reset] = Field(None, description="Represents the reset and observation values that were used to determine the transfer amount.")
  """
  Represents the reset and observation values that were used to determine the transfer amount.
  """
  settlementOrigin: Optional[SettlementOrigin] = Field(None, description="Represents the origin to the transfer as a reference for lineage purposes, whether it originated from trade level settlement terms or from payment terms on an economic payout.")
  """
  Represents the origin to the transfer as a reference for lineage purposes, whether it originated from trade level settlement terms or from payment terms on an economic payout.
  """
  transferExpression: TransferExpression = Field(..., description="Specifies a transfer expression (cash price, performance amount, scheduled payment amount, etc.) to define the nature of the transfer amount and its source.")
  """
  Specifies a transfer expression (cash price, performance amount, scheduled payment amount, etc.) to define the nature of the transfer amount and its source.
  """

from cdm.event.common.Reset import Reset
from cdm.event.common.SettlementOrigin import SettlementOrigin
from cdm.event.common.TransferExpression import TransferExpression

Transfer.update_forward_refs()
