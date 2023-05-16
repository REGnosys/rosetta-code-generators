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

__all__ = ['SingleValuationDate']


class SingleValuationDate(BaseDataClass):
  """
  A class to specify the number of business days after satisfaction of all conditions to settlement.
  """
  businessDays: Optional[int] = Field(None, description="A number of business days. Its precise meaning is dependant on the context in which this element is used. ISDA 2003 Term: Business Day.")
  """
  A number of business days. Its precise meaning is dependant on the context in which this element is used. ISDA 2003 Term: Business Day.
  """
  
  @rosetta_condition
  def condition_0_NonNegativeBusinessDays(self):
    """
    FpML specifies businessDays as a NonNegativeInteger.
    """
    def _then_fn0():
      return all_elements(self.businessDays, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.businessDays) is not None), _then_fn0, _else_fn0)


SingleValuationDate.update_forward_refs()
