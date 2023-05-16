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

__all__ = ['BoundedVariance']


class BoundedVariance(BaseDataClass):
  daysInRangeAdjustment: bool = Field(..., description="The contract specifies whether the notional should be scaled by the Number of Days in Range divided by the Expected N. The number of Days in Ranges refers to the number of returns that contribute to the realized volatility.")
  """
  The contract specifies whether the notional should be scaled by the Number of Days in Range divided by the Expected N. The number of Days in Ranges refers to the number of returns that contribute to the realized volatility.
  """
  lowerBarrier: Optional[Decimal] = Field(None, description="All observations below this price level will be excluded from the variance calculation.")
  """
  All observations below this price level will be excluded from the variance calculation.
  """
  realisedVarianceMethod: RealisedVarianceMethodEnum = Field(..., description="The contract specifies which price must satisfy the boundary condition.")
  """
  The contract specifies which price must satisfy the boundary condition.
  """
  upperBarrier: Optional[Decimal] = Field(None, description="All observations above this price level will be excluded from the variance calculation.")
  """
  All observations above this price level will be excluded from the variance calculation.
  """
  
  @rosetta_condition
  def condition_0_NonNegativeBarriers(self):
    """
    Barriers cannot be set to negative values
    """
    def _then_fn1():
      return all_elements(self.lowerBarrier, ">=", 0)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (all_elements(self.upperBarrier, ">=", 0) and if_cond_fn(((self.lowerBarrier) is not None), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.upperBarrier) is not None), _then_fn0, _else_fn0)

from cdm.product.asset.RealisedVarianceMethodEnum import RealisedVarianceMethodEnum

BoundedVariance.update_forward_refs()
