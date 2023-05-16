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

__all__ = ['ValuationDates']


class ValuationDates(BaseDataClass):
  """
  Defines how and when a performance type option or performance type swap is to be valued, including both interim and final valuation dates.
  """
  valuationDatesFinal: PerformanceValuationDates = Field(..., description="Specifies the final valuation dates of the underlyer.")
  """
  Specifies the final valuation dates of the underlyer.
  """
  valuationDatesInterim: Optional[PerformanceValuationDates] = Field(None, description="Specifies the interim valuation dates of the underlyer.")
  """
  Specifies the interim valuation dates of the underlyer.
  """

from cdm.observable.asset.PerformanceValuationDates import PerformanceValuationDates

ValuationDates.update_forward_refs()
