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

__all__ = ['Frequency']


class Frequency(BaseDataClass):
  """
  A class for defining a date frequency, e.g. one day, three months, through the combination of an integer value and a standardized period value that is specified as part of an enumeration.
  """
  period: PeriodExtendedEnum = Field(..., description="A time period, e.g. a day, week, month, year or term of the stream.")
  """
  A time period, e.g. a day, week, month, year or term of the stream.
  """
  periodMultiplier: int = Field(..., description="A time period multiplier, e.g. 1, 2, or 3. If the period value is T (Term) then period multiplier must contain the value 1.")
  """
  A time period multiplier, e.g. 1, 2, or 3. If the period value is T (Term) then period multiplier must contain the value 1.
  """
  
  @rosetta_condition
  def condition_0_TermPeriod(self):
    """
    FpML specifies that if period value is T (Term) then periodMultiplier must contain the value 1.
    """
    def _then_fn0():
      return all_elements(self.periodMultiplier, "=", 1)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.period, "=", PeriodExtendedEnum.T), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_PositivePeriodMultiplier(self):
    """
    FpML specifies periodMultiplier as a positive integer.
    """
    return all_elements(self.periodMultiplier, ">", 0)

from cdm.base.datetime.PeriodExtendedEnum import PeriodExtendedEnum

Frequency.update_forward_refs()
