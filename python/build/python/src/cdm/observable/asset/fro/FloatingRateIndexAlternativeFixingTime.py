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

__all__ = ['FloatingRateIndexAlternativeFixingTime']

from cdm.observable.asset.fro.FloatingRateIndexFixingTime import FloatingRateIndexFixingTime

class FloatingRateIndexAlternativeFixingTime(FloatingRateIndexFixingTime):
  """
  This type holds parameters defining the alternative fixing time for a floating rate index.
  """
  fallbackReason: Optional[str] = Field(None, description="Allows a reason to be specified for using the alternative fixing time.")
  """
  Allows a reason to be specified for using the alternative fixing time.
  """


FloatingRateIndexAlternativeFixingTime.update_forward_refs()
