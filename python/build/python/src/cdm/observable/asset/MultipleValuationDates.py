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

__all__ = ['MultipleValuationDates']

from cdm.observable.asset.SingleValuationDate import SingleValuationDate

class MultipleValuationDates(SingleValuationDate):
  businessDaysThereafter: Optional[int] = Field(None, description="The number of business days between successive valuation dates when multiple valuation dates are applicable for cash settlement. ISDA 2003 Term: Business Days thereafter.")
  """
  The number of business days between successive valuation dates when multiple valuation dates are applicable for cash settlement. ISDA 2003 Term: Business Days thereafter.
  """
  numberValuationDates: Optional[int] = Field(None, description="Where multiple valuation dates are specified as being applicable for cash settlement, this element specifies (a) the number of applicable valuation dates, and (b) the number of business days after satisfaction of all conditions to settlement when the first such valuation date occurs, and (c) the number of business days thereafter of each successive valuation date. ISDA 2003 Term: Multiple Valuation Dates.")
  """
  Where multiple valuation dates are specified as being applicable for cash settlement, this element specifies (a) the number of applicable valuation dates, and (b) the number of business days after satisfaction of all conditions to settlement when the first such valuation date occurs, and (c) the number of business days thereafter of each successive valuation date. ISDA 2003 Term: Multiple Valuation Dates.
  """
  
  @rosetta_condition
  def condition_0_BusinessDaysThereafter(self):
    """
    FpML specifies businessDaysThereafter as a PositiveInteger.
    """
    def _then_fn0():
      return all_elements(self.businessDaysThereafter, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.businessDaysThereafter) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_NumberValuationDates(self):
    """
    FpML specifies numberValuationDates as a PositiveInteger.
    """
    def _then_fn0():
      return all_elements(self.numberValuationDates, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.numberValuationDates) is not None), _then_fn0, _else_fn0)


MultipleValuationDates.update_forward_refs()
