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

__all__ = ['DateTimeList']


class DateTimeList(BaseDataClass):
  """
  List of dateTimes.
  """
  dateTime: List[datetime] = Field([], description="The CDM specifies that the zoned date time is to be expressed in accordance with ISO 8601, either as UTC as an offset to UTC.")
  """
  The CDM specifies that the zoned date time is to be expressed in accordance with ISO 8601, either as UTC as an offset to UTC.
  """
  @rosetta_condition
  def cardinality_dateTime(self):
    return check_cardinality(self.dateTime, 1, None)
  


DateTimeList.update_forward_refs()
