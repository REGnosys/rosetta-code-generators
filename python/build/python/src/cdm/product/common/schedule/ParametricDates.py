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

__all__ = ['ParametricDates']


class ParametricDates(BaseDataClass):
  """
  Defines rules for the dates on which the price will be determined.
  """
  businessCenters: BusinessCenters = Field(..., description="The enumerated values to specify the business centers.")
  """
  The enumerated values to specify the business centers.
  """
  dayDistribution: Optional[DayDistributionEnum] = Field(None, description="Denotes the method by which the pricing days are distributed across the pricing period.")
  """
  Denotes the method by which the pricing days are distributed across the pricing period.
  """
  dayFrequency: Optional[Decimal] = Field(None, description="Defines the occurrence of the dayOfWeek within the pricing period on which pricing will take place, e.g. the 3rd Friday within each Calculation Period. If omitted, every dayOfWeek will be a pricing day.")
  """
  Defines the occurrence of the dayOfWeek within the pricing period on which pricing will take place, e.g. the 3rd Friday within each Calculation Period. If omitted, every dayOfWeek will be a pricing day.
  """
  dayOfWeek: List[DayOfWeekEnum] = Field([], description="Indicates the days of the week on which the price will be determined.")
  """
  Indicates the days of the week on which the price will be determined.
  """
  @rosetta_condition
  def cardinality_dayOfWeek(self):
    return check_cardinality(self.dayOfWeek, 0, 7)
  
  dayType: DayTypeEnum = Field(..., description="Denotes the enumerated values to specify the day type classification used in counting the number of days between two dates.")
  """
  Denotes the enumerated values to specify the day type classification used in counting the number of days between two dates.
  """
  lag: Optional[Lag] = Field(None, description="The pricing period per calculation period if the pricing days do not wholly fall within the respective calculation period.")
  """
  The pricing period per calculation period if the pricing days do not wholly fall within the respective calculation period.
  """
  
  @rosetta_condition
  def condition_0_ParametricDatesChoice(self):
    return self.check_one_of_constraint('dayDistribution', 'dayOfWeek', necessity=True)
  
  @rosetta_condition
  def condition_1_DayOfWeekMethod(self):
    def _then_fn0():
      return ((self.dayFrequency) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.dayOfWeek) is not None), _then_fn0, _else_fn0)

from cdm.base.datetime.BusinessCenters import BusinessCenters
from cdm.product.asset.DayDistributionEnum import DayDistributionEnum
from cdm.base.datetime.DayOfWeekEnum import DayOfWeekEnum
from cdm.base.datetime.DayTypeEnum import DayTypeEnum
from cdm.product.common.schedule.Lag import Lag

ParametricDates.update_forward_refs()
