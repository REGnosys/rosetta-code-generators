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

__all__ = ['CalculationPeriodFrequency']

from cdm.base.datetime.Frequency import Frequency

class CalculationPeriodFrequency(Frequency):
  """
  A class to specify the frequency at which calculation period end dates occur within the regular part of the calculation period schedule and their roll date convention.
  """
  balanceOfFirstPeriod: Optional[bool] = Field(None, description="Indicates, when true, that that the first Calculation Period should run from the Effective Date to the end of the calendar period in which the Effective Date falls, e.g. Jan 15 - Jan 31 if the calculation periods are one month long and Effective Date is Jan 15. If false, the first Calculation Period should run from the Effective Date for one whole period, e.g. Jan 15 to Feb 14 if the calculation periods are one month long and Effective Date is Jan 15. Mostly used in Commmodity Swaps.")
  """
  Indicates, when true, that that the first Calculation Period should run from the Effective Date to the end of the calendar period in which the Effective Date falls, e.g. Jan 15 - Jan 31 if the calculation periods are one month long and Effective Date is Jan 15. If false, the first Calculation Period should run from the Effective Date for one whole period, e.g. Jan 15 to Feb 14 if the calculation periods are one month long and Effective Date is Jan 15. Mostly used in Commmodity Swaps.
  """
  rollConvention: RollConventionEnum = Field(..., description="The roll convention specifies the period term as part of a periodic schedule, i.e. the calculation period end date within the regular part of the calculation period. The value could be a rule, e.g. IMM Settlement Dates, which is the 3rd Wednesday of the month, or it could be a specific day of the month, such as the first day of the applicable month. It is used in conjunction with a frequency and the regular period start date of a calculation period.")
  """
  The roll convention specifies the period term as part of a periodic schedule, i.e. the calculation period end date within the regular part of the calculation period. The value could be a rule, e.g. IMM Settlement Dates, which is the 3rd Wednesday of the month, or it could be a specific day of the month, such as the first day of the applicable month. It is used in conjunction with a frequency and the regular period start date of a calculation period.
  """
  
  @rosetta_condition
  def condition_0_FpML_ird_57(self):
    """
    FpML validation rule ird-57 - Context: CalculationPeriodFrequency. [period eq ('M', 'Y')] not(rollConvention = ('NONE', 'SFE', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN')).
    """
    def _then_fn0():
      return ((((((((any_elements(self.rollConvention, "<>", RollConventionEnum.NONE) and any_elements(self.rollConvention, "<>", RollConventionEnum.SFE)) and any_elements(self.rollConvention, "<>", RollConventionEnum.MON)) and any_elements(self.rollConvention, "<>", RollConventionEnum.TUE)) and any_elements(self.rollConvention, "<>", RollConventionEnum.WED)) and any_elements(self.rollConvention, "<>", RollConventionEnum.THU)) and any_elements(self.rollConvention, "<>", RollConventionEnum.FRI)) and any_elements(self.rollConvention, "<>", RollConventionEnum.SAT)) and any_elements(self.rollConvention, "<>", RollConventionEnum.SUN))
    
    def _else_fn0():
      return True
    
    return if_cond_fn((all_elements(self.period, "=", PeriodExtendedEnum.M) or all_elements(self.period, "=", PeriodExtendedEnum.Y)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_FpML_ird_58(self):
    """
    FpML validation rule ird-58 - Context: CalculationPeriodFrequency. When the period is 'W', the rollConvention must be a week day, 'SFE' or 'NONE'.
    """
    def _then_fn0():
      return ((((((((all_elements(self.rollConvention, "=", RollConventionEnum.NONE) or all_elements(self.rollConvention, "=", RollConventionEnum.SFE)) or all_elements(self.rollConvention, "=", RollConventionEnum.MON)) or all_elements(self.rollConvention, "=", RollConventionEnum.TUE)) or all_elements(self.rollConvention, "=", RollConventionEnum.WED)) or all_elements(self.rollConvention, "=", RollConventionEnum.THU)) or all_elements(self.rollConvention, "=", RollConventionEnum.FRI)) or all_elements(self.rollConvention, "=", RollConventionEnum.SAT)) or all_elements(self.rollConvention, "=", RollConventionEnum.SUN))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.period, "=", PeriodExtendedEnum.W), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_FpML_ird_60(self):
    """
    FpML validation rule ird-60 - Context: CalculationPeriodFrequency. When the period is 'T', the rollConvention must be 'NONE'.
    """
    def _then_fn0():
      return all_elements(self.rollConvention, "=", RollConventionEnum.NONE)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.period, "=", PeriodExtendedEnum.T), _then_fn0, _else_fn0)

from cdm.base.datetime.RollConventionEnum import RollConventionEnum
from cdm.base.datetime.PeriodExtendedEnum import PeriodExtendedEnum

CalculationPeriodFrequency.update_forward_refs()
