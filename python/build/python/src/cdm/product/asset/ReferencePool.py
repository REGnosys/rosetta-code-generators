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

__all__ = ['ReferencePool']


class ReferencePool(BaseDataClass):
  """
  This type contains all the reference pool items to define the reference entity and reference obligation(s) in the basket.
  """
  referencePoolItem: List[ReferencePoolItem] = Field([], description="This type contains all the constituent weight and reference information.")
  """
  This type contains all the constituent weight and reference information.
  """
  @rosetta_condition
  def cardinality_referencePoolItem(self):
    return check_cardinality(self.referencePoolItem, 1, None)
  
  
  @rosetta_condition
  def condition_0_FpML_cd_44_openUnits(self):
    """
    FpML validation rule cd-44 - All referencePoolItem/constituentWeight must have the same name of child element.
    """
    def _then_fn0():
      return ((self.referencePoolItem.constituentWeight.basketPercentage) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.referencePoolItem.constituentWeight.openUnits) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_FpML_cd_44_basketPercentage(self):
    """
    FpML validation rule cd-44 - All referencePoolItem/constituentWeight must have the same name of child element.
    """
    def _then_fn0():
      return ((self.referencePoolItem.constituentWeight.openUnits) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.referencePoolItem.constituentWeight.basketPercentage) is not None), _then_fn0, _else_fn0)

from cdm.product.asset.ReferencePoolItem import ReferencePoolItem

ReferencePool.update_forward_refs()
