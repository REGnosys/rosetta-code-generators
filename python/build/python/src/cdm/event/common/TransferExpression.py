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

__all__ = ['TransferExpression']


class TransferExpression(BaseDataClass):
  """
  Specifies a transfer expression (cash price, performance amount, scheduled payment amount, etc.) to define the nature of the transfer amount and its source.
  """
  priceTransfer: Optional[FeeTypeEnum] = Field(None, description="Specifies a transfer amount exchanged as a price or fee for entering into a Business Event, e.g. Premium, Termination fee, Novation fee.")
  """
  Specifies a transfer amount exchanged as a price or fee for entering into a Business Event, e.g. Premium, Termination fee, Novation fee.
  """
  scheduledTransfer: Optional[ScheduledTransfer] = Field(None, description="Specifies a transfer created from a scheduled or contingent event on a contract, e.g. Exercise, Performance, Credit Event")
  """
  Specifies a transfer created from a scheduled or contingent event on a contract, e.g. Exercise, Performance, Credit Event
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('priceTransfer', 'scheduledTransfer', necessity=True)

from cdm.observable.asset.FeeTypeEnum import FeeTypeEnum
from cdm.event.common.ScheduledTransfer import ScheduledTransfer

TransferExpression.update_forward_refs()
