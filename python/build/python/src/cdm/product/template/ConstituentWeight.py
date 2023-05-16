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

__all__ = ['ConstituentWeight']


class ConstituentWeight(BaseDataClass):
  """
  A class describing the weight of each of the underlier constituent within the basket, either in absolute or relative terms.
  """
  basketPercentage: Optional[Decimal] = Field(None, description="The relative weight of each respective basket constituent, expressed in percentage. A basket percentage of 5% would be represented as 0.05.")
  """
  The relative weight of each respective basket constituent, expressed in percentage. A basket percentage of 5% would be represented as 0.05.
  """
  openUnits: Optional[Decimal] = Field(None, description="The number of units (index or securities) that constitute the underlier of the swap. In the case of a basket swap, this element is used to reference both the number of basket units, and the number of each asset components of the basket when these are expressed in absolute terms.")
  """
  The number of units (index or securities) that constitute the underlier of the swap. In the case of a basket swap, this element is used to reference both the number of basket units, and the number of each asset components of the basket when these are expressed in absolute terms.
  """
  
  @rosetta_condition
  def condition_0_BasketPercentage(self):
    """
    FpML specifies basketPercentage as a RestrictedPercentage type, meaning that the value needs to be comprised between 0 and 1.
    """
    def _then_fn0():
      return (all_elements(self.basketPercentage, ">=", 0.0) and all_elements(self.basketPercentage, "<=", 1.0))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.basketPercentage) is not None), _then_fn0, _else_fn0)


ConstituentWeight.update_forward_refs()
