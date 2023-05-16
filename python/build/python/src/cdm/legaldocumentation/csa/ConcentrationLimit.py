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

__all__ = ['ConcentrationLimit']


class ConcentrationLimit(BaseDataClass):
  """
  Represents a class to describe concentration limits that may be applicable to eligible collateral criteria.
  """
  concentrationLimitCriteria: List[ConcentrationLimitCriteria] = Field([], description="Specifies a set of criteria to describe the assets that the concentration limits apply to.")
  """
  Specifies a set of criteria to describe the assets that the concentration limits apply to.
  """
  percentageLimit: Optional[NumberRange] = Field(None, description="Specifies the perecentage of collateral limit represented as a decimal number - example 25% is 0.25.")
  """
  Specifies the perecentage of collateral limit represented as a decimal number - example 25% is 0.25.
  """
  valueLimit: Optional[MoneyRange] = Field(None, description="Specifies the value of collateral limit represented as a range.")
  """
  Specifies the value of collateral limit represented as a range.
  """
  
  @rosetta_condition
  def condition_0_ConcentrationLimitValueChoice(self):
    """
    Either a value or percentage concentration limit must be specified.
    """
    return self.check_one_of_constraint('valueLimit', 'percentageLimit', necessity=True)
  
  @rosetta_condition
  def condition_1_PercentageConcentrationLimit(self):
    """
    concentration limit must be described as a percentage.
    """
    def _then_fn0():
      return ((self.percentageLimit) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements((self.concentrationLimitCriteria.concentrationLimitType), "=", ConcentrationLimitTypeEnum.MARKET_CAPITALISATION), _then_fn0, _else_fn0)

from cdm.legaldocumentation.csa.ConcentrationLimitCriteria import ConcentrationLimitCriteria
from cdm.base.math.NumberRange import NumberRange
from cdm.base.math.MoneyRange import MoneyRange
from cdm.legaldocumentation.csa.ConcentrationLimitTypeEnum import ConcentrationLimitTypeEnum

ConcentrationLimit.update_forward_refs()
