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

__all__ = ['BespokeCalculationDate']


class BespokeCalculationDate(BaseDataClass):
  """
  A class to specify bespoke Calculation Date terms for the purposes of Initial Margin
  """
  calculationDateImTerms: Optional[str] = Field(None, description="The Additional Calculation Date terms for the purposes of Initial Margin")
  """
  The Additional Calculation Date terms for the purposes of Initial Margin
  """
  isApplicable: bool = Field(..., description="Additional Calculation Date terms are applicable when True and not applicable when False")
  """
  Additional Calculation Date terms are applicable when True and not applicable when False
  """
  
  @rosetta_condition
  def condition_0_CalculationDateImTerms(self):
    """
    A data rule to enforce that Additional Calculation Date Terms should be absent when not applicable
    """
    def _then_fn0():
      return ((self.calculationDateImTerms) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)


BespokeCalculationDate.update_forward_refs()
