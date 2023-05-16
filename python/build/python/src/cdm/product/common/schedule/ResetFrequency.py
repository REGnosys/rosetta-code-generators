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

__all__ = ['ResetFrequency']

from cdm.base.datetime.Frequency import Frequency

class ResetFrequency(Frequency):
  """
  A class defining the reset frequency. In the case of a weekly reset, also specifies the day of the week that the reset occurs. If the reset frequency is greater than the calculation period frequency the this implies that more or more reset dates is established for each calculation period and some form of rate averaging is applicable. The specific averaging method of calculation is specified in FloatingRateCalculation. In case the reset frequency is of value T (term), the period is defined by the swap/swapStream/calculationPerioDates/effectiveDate and the swap/swapStream/calculationPerioDates/terminationDate.
  """
  weeklyRollConvention: Optional[WeeklyRollConventionEnum] = Field(None, description="The day of the week on which a weekly reset date occurs. This element must be included if the reset frequency is defined as weekly and not otherwise.")
  """
  The day of the week on which a weekly reset date occurs. This element must be included if the reset frequency is defined as weekly and not otherwise.
  """
  
  @rosetta_condition
  def condition_0_FpML_ird_49(self):
    """
    FpML validation rule ird-49 - WeeklyRollConvention should exist if and only if the period is 'W'.
    """
    def _then_fn0():
      return all_elements(self.period, "=", PeriodExtendedEnum.W)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.weeklyRollConvention) is not None), _then_fn0, _else_fn0)

from cdm.product.common.schedule.WeeklyRollConventionEnum import WeeklyRollConventionEnum
from cdm.base.datetime.PeriodExtendedEnum import PeriodExtendedEnum

ResetFrequency.update_forward_refs()
