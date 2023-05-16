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

__all__ = ['FloatingRateIndexFixingDetails']


class FloatingRateIndexFixingDetails(BaseDataClass):
  """
  This type holds parameters defining the fixingt time and offset for a floating rate index.
  """
  fixingOffset: Optional[BusinessDayOffset] = Field(None, description="Parameters defining the normal fixing offset (can vary by index tenor / designated maturity).")
  """
  Parameters defining the normal fixing offset (can vary by index tenor / designated maturity).
  """
  fixingTime: Optional[FloatingRateIndexFixingTime] = Field(None, description="Parameters defining the normal fixing time (can vary by index tenor / designated maturity).")
  """
  Parameters defining the normal fixing time (can vary by index tenor / designated maturity).
  """

from cdm.observable.asset.fro.BusinessDayOffset import BusinessDayOffset
from cdm.observable.asset.fro.FloatingRateIndexFixingTime import FloatingRateIndexFixingTime

FloatingRateIndexFixingDetails.update_forward_refs()
