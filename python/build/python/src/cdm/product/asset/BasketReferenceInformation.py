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

__all__ = ['BasketReferenceInformation']


class BasketReferenceInformation(BaseDataClass):
  """
  CDS Basket Reference Information.
  """
  basketId: List[AttributeWithMeta[str] | str] = Field([], description="A CDS basket identifier.")
  """
  A CDS basket identifier.
  """
  basketName: Optional[AttributeWithMeta[str] | str] = Field(None, description="The name of the basket expressed as a free format string. FpML does not define usage rules for this element.")
  """
  The name of the basket expressed as a free format string. FpML does not define usage rules for this element.
  """
  mthToDefault: Optional[int] = Field(None, description="M th reference obligation to default to allow representation of N th to M th defaults.")
  """
  M th reference obligation to default to allow representation of N th to M th defaults.
  """
  nthToDefault: Optional[int] = Field(None, description="N th reference obligation to default triggers payout.")
  """
  N th reference obligation to default triggers payout.
  """
  referencePool: ReferencePool = Field(..., description="This element contains all the reference pool items to define the reference entity and reference obligation(s) in the basket.")
  """
  This element contains all the reference pool items to define the reference entity and reference obligation(s) in the basket.
  """
  tranche: Optional[Tranche] = Field(None, description="This element contains CDS tranche terms.")
  """
  This element contains CDS tranche terms.
  """
  
  @rosetta_condition
  def condition_0_BasketReferenceInformationChoice(self):
    """
    Choice rule to represent an FpML choice construct. This choice rule is complemented by the data rule BasketReferenceInformation_nthToDefault to represent the FpML construct where there is a choice between a tranche element and a [required nthToDefault, optional mthToDefault] branch.
    """
    return self.check_one_of_constraint('nthToDefault', 'tranche', necessity=True)
  
  @rosetta_condition
  def condition_1_NthToDefault(self):
    """
    As part of the branch of the choice node, FpML requires the nthToDefault element to be present, while the mthToDefault one is optional.
    """
    def _then_fn0():
      return ((self.nthToDefault) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.mthToDefault) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_MthToDefault(self):
    """
    FpML validation rule cd-39 - Context: BasketReferenceInformation (complex type). If nthToDefault exists, and if mthToDefault exists, then nthToDefault must be less than mthToDefault.
    """
    def _then_fn0():
      return all_elements(self.nthToDefault, "<", self.mthToDefault)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.nthToDefault) is not None) and ((self.mthToDefault) is not None)), _then_fn0, _else_fn0)

from cdm.product.asset.ReferencePool import ReferencePool
from cdm.product.asset.Tranche import Tranche

BasketReferenceInformation.update_forward_refs()
