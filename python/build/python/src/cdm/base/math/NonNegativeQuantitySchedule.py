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

__all__ = ['NonNegativeQuantitySchedule']

from cdm.base.math.QuantitySchedule import QuantitySchedule

class NonNegativeQuantitySchedule(QuantitySchedule):
  
  @rosetta_condition
  def condition_0_NonNegativeQuantity_amount(self):
    """
    For a non-negative quantity, all amount attribute must be positive.
    """
    def _then_fn1():
      return all_elements(self.datedValue.value, ">=", 0.0)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (all_elements(self.value, ">=", 0.0) and if_cond_fn(((self.datedValue) is not None), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.value) is not None), _then_fn0, _else_fn0)


NonNegativeQuantitySchedule.update_forward_refs()
