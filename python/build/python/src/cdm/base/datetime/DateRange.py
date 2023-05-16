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

__all__ = ['DateRange']


class DateRange(BaseDataClass):
  """
  A class defining a contiguous series of calendar dates. The date range is defined as all the dates between and including the start and the end date. The start date must fall on or before the end date.
  """
  endDate: date = Field(..., description="The last date of a date range.")
  """
  The last date of a date range.
  """
  startDate: date = Field(..., description="The first date of a date range.")
  """
  The first date of a date range.
  """
  
  @rosetta_condition
  def condition_0_DatesOrdered(self):
    """
    The start date must fall on or before the end date (a date range of only one date is allowed).
    """
    return all_elements(self.startDate, "<=", self.endDate)


DateRange.update_forward_refs()
