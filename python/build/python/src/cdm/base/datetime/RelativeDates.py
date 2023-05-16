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

__all__ = ['RelativeDates']

from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset

class RelativeDates(RelativeDateOffset):
  """
  A class describing a set of dates defined as relative to another set of dates.
  """
  periodSkip: Optional[int] = Field(None, description="The number of periods in the referenced date schedule that are between each date in the relative date schedule. Thus a skip of 2 would mean that dates are relative to every second date in the referenced schedule. If present this should have a value greater than 1.")
  """
  The number of periods in the referenced date schedule that are between each date in the relative date schedule. Thus a skip of 2 would mean that dates are relative to every second date in the referenced schedule. If present this should have a value greater than 1.
  """
  scheduleBounds: Optional[DateRange] = Field(None, description="The first and last dates of a schedule. This can be used to restrict the range of values in a reference series of dates.")
  """
  The first and last dates of a schedule. This can be used to restrict the range of values in a reference series of dates.
  """
  
  @rosetta_condition
  def condition_0_PeriodSkipGreaterThanOne(self):
    """
    FpML specifies that, if present, the period skip should have a value greater than 1.
    """
    def _then_fn0():
      return all_elements(self.periodSkip, ">", 1)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.periodSkip) is not None), _then_fn0, _else_fn0)

from cdm.base.datetime.DateRange import DateRange

RelativeDates.update_forward_refs()
