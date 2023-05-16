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

__all__ = ['FixedPrice']


class FixedPrice(BaseDataClass):
  """
  A predefined price accorded by the counterparties.
  """
  price: Optional[AttributeWithAddress[PriceSchedule] | PriceSchedule] = Field(None, description="Fixed price step schedule, including an initial price specified as an absolute number.")
  """
  Fixed price step schedule, including an initial price specified as an absolute number.
  """
  
  @rosetta_condition
  def condition_0_NonNegativePrice_amount(self):
    """
    For a non-negative price, the amount attribute must be positive.
    """
    def _then_fn1():
      return all_elements(self.price.datedValue.value, ">=", 0.0)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (all_elements(self.price.value, ">=", 0.0) and if_cond_fn(((self.price.datedValue) is not None), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.price.value) is not None), _then_fn0, _else_fn0)

from cdm.observable.asset.PriceSchedule import PriceSchedule

FixedPrice.update_forward_refs()
