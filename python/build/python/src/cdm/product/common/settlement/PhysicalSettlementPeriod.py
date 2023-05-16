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

__all__ = ['PhysicalSettlementPeriod']


class PhysicalSettlementPeriod(BaseDataClass):
  businessDays: Optional[int] = Field(None, description="A number of business days. Its precise meaning is dependant on the context in which this element is used. ISDA 2003 Term: Business Day.")
  """
  A number of business days. Its precise meaning is dependant on the context in which this element is used. ISDA 2003 Term: Business Day.
  """
  businessDaysNotSpecified: Optional[bool] = Field(None, description="An explicit indication that a number of business days are not specified and therefore ISDA fallback provisions should apply.")
  """
  An explicit indication that a number of business days are not specified and therefore ISDA fallback provisions should apply.
  """
  maximumBusinessDays: Optional[int] = Field(None, description="A maximum number of business days. Its precise meaning is dependant on the context in which this element is used. Intended to be used to limit a particular ISDA fallback provision.")
  """
  A maximum number of business days. Its precise meaning is dependant on the context in which this element is used. Intended to be used to limit a particular ISDA fallback provision.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('businessDaysNotSpecified', 'businessDays', 'maximumBusinessDays', necessity=True)
  
  @rosetta_condition
  def condition_1_BusinessDays(self):
    """
    FpML specifies businessDays as a NonNegativeInteger.
    """
    def _then_fn0():
      return all_elements(self.businessDays, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.businessDays) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_MaximumBusinessDays(self):
    """
    FpML specifies maximumBusinessDays as a NonNegativeInteger.
    """
    def _then_fn0():
      return all_elements(self.maximumBusinessDays, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.maximumBusinessDays) is not None), _then_fn0, _else_fn0)


PhysicalSettlementPeriod.update_forward_refs()
