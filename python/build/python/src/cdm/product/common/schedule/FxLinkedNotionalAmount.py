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

__all__ = ['FxLinkedNotionalAmount']


class FxLinkedNotionalAmount(BaseDataClass):
  """
  A data to:  describe the cashflow representation for FX linked notionals.
  """
  adjustedFxSpotFixingDate: Optional[date] = Field(None, description="The date on which the FX spot rate is observed. This date should already be adjusted for any applicable business day convention.")
  """
  The date on which the FX spot rate is observed. This date should already be adjusted for any applicable business day convention.
  """
  notionalAmount: Optional[Decimal] = Field(None, description="The calculation period notional amount.")
  """
  The calculation period notional amount.
  """
  observedFxSpotRate: Optional[Decimal] = Field(None, description="The actual observed FX spot rate.")
  """
  The actual observed FX spot rate.
  """
  resetDate: Optional[date] = Field(None, description="The reset date.")
  """
  The reset date.
  """


FxLinkedNotionalAmount.update_forward_refs()
