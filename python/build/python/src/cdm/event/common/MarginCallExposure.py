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

__all__ = ['MarginCallExposure']

from cdm.event.common.MarginCallBase import MarginCallBase

class MarginCallExposure(MarginCallBase):
  """
  Represents attributes required for mark to market value or IM calculation value of the trade portfolio as recorded by the principle (in base currency).
  """
  overallExposure: Exposure = Field(..., description="Represents the whole overall mark to market value or IM calculation value of the trade portfolio as recorded by the principle (in base currency).")
  """
  Represents the whole overall mark to market value or IM calculation value of the trade portfolio as recorded by the principle (in base currency).
  """
  scheduleGridIMExposure: Optional[Exposure] = Field(None, description="Represents Initial Margin (IM) exposure derived from schedule or Grid calculation.")
  """
  Represents Initial Margin (IM) exposure derived from schedule or Grid calculation.
  """
  simmIMExposure: Optional[Exposure] = Field(None, description="Represents Initial Margin (IM) exposure derived from ISDA SIMM calculation.")
  """
  Represents Initial Margin (IM) exposure derived from ISDA SIMM calculation.
  """
  
  @rosetta_condition
  def condition_0_OverallExposureSumOfSimmAndScheduleIM(self):
    """
    Represents a condition to ensure that if Simm IM exposure and Schedule/Grid IM exposure are specified the sum value must equate to overall exposure amount.
    """
    def _then_fn0():
      return ((all_elements(self.overallExposure.aggregateValue.value, "=", (self.simmIMExposure.aggregateValue.value + self.scheduleGridIMExposure.aggregateValue.value)) and all_elements(self.overallExposure.aggregateValue.unit.currency, "=", self.simmIMExposure.aggregateValue.unit.currency)) and all_elements(self.overallExposure.aggregateValue.unit.currency, "=", self.scheduleGridIMExposure.aggregateValue.unit.currency))
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.simmIMExposure) is not None) and ((self.scheduleGridIMExposure) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_ExposureSimmAndScheduleIMOnly(self):
    """
    Specifies a condition to ensure that if margin exposure is defined as Simm IM and Schedule/Grid IM Exposure this is only applicable if the Reg margin type is defined as RegIM (Regulatory Initial Margin).
    """
    def _then_fn0():
      return all_elements(self.regMarginType, "=", RegMarginTypeEnum.REG_IM)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.simmIMExposure) is not None) and ((self.scheduleGridIMExposure) is not None)), _then_fn0, _else_fn0)

from cdm.event.common.Exposure import Exposure
from cdm.event.common.RegMarginTypeEnum import RegMarginTypeEnum

MarginCallExposure.update_forward_refs()
