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

__all__ = ['OffsetCalculation']


class OffsetCalculation(BaseDataClass):
  """
  Defines business day shifts for daily componded or averaged rates.  This type is used for lookback and lockout rates. This type is used to represent modular computed rates in interestRatePayouts.
  """
  offsetDays: Optional[int] = Field(None, description="The number of business days offset.")
  """
  The number of business days offset.
  """


OffsetCalculation.update_forward_refs()
