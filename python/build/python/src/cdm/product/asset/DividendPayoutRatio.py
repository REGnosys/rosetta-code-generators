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

__all__ = ['DividendPayoutRatio']


class DividendPayoutRatio(BaseDataClass):
  """
  A class describing the dividend payout ratio associated with an equity underlier. In certain cases the actual ratio is not known on trade inception, and only general conditions are then specified.
  """
  basketConstituent: Optional[Product] = Field(None, description="In the case of a basket underlier, specifies to which component of the basket this particular set of dividend payout ratios correspond.")
  """
  In the case of a basket underlier, specifies to which component of the basket this particular set of dividend payout ratios correspond.
  """
  cashRatio: Optional[Decimal] = Field(None, description="Specifies the cash actual dividend payout ratio associated with the equity underlier. A ratio of 90% should be expressed at 0.90.")
  """
  Specifies the cash actual dividend payout ratio associated with the equity underlier. A ratio of 90% should be expressed at 0.90.
  """
  nonCashRatio: Optional[Decimal] = Field(None, description="Specifies the non cash actual dividend payout ratio associated with the equity underlier. A ratio of 90% should be expressed at 0.90.")
  """
  Specifies the non cash actual dividend payout ratio associated with the equity underlier. A ratio of 90% should be expressed at 0.90.
  """
  totalRatio: Decimal = Field(..., description="Specifies the total actual dividend payout ratio associated with the equity underlier. A ratio of 90% should be expressed at 0.90.")
  """
  Specifies the total actual dividend payout ratio associated with the equity underlier. A ratio of 90% should be expressed at 0.90.
  """
  
  @rosetta_condition
  def condition_0_DividendPayoutRatioTotal(self):
    """
    The dividend payout ratio should be comprised between 0 and 100%, meaning 0 and 1.
    """
    return (all_elements(self.totalRatio, ">=", 0) and all_elements(self.totalRatio, "<=", 1))
  
  @rosetta_condition
  def condition_1_DividendPayoutRatioCash(self):
    """
    The cash dividend payout ratio should be comprised between 0 and 100%, meaning 0 and 1.
    """
    def _then_fn0():
      return (all_elements(self.cashRatio, ">=", 0) and all_elements(self.totalRatio, "<=", 1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.cashRatio) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_DividendPayoutRatioNonCash(self):
    """
    The non cash dividend payout ratio should be comprised between 0 and 100%, meaning 0 and 1.
    """
    def _then_fn0():
      return (all_elements(self.nonCashRatio, ">=", 0) and all_elements(self.totalRatio, "<=", 1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.nonCashRatio) is not None), _then_fn0, _else_fn0)

from cdm.product.template.Product import Product

DividendPayoutRatio.update_forward_refs()
