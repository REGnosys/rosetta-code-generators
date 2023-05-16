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

__all__ = ['AdditionalType']


class AdditionalType(BaseDataClass):
  """
  The specification of the Additional Type of transaction that can require the collection or delivery of initial margin under a given regulatory regime for the purposes of Covered Transactions, as specified in ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (b)(B).
  """
  customValue: Optional[str] = Field(None, description="The qualification of the Additional Type of transaction that can require the collection or delivery of initial margin when specified as a custom value by the parties to the legal agreement.")
  """
  The qualification of the Additional Type of transaction that can require the collection or delivery of initial margin when specified as a custom value by the parties to the legal agreement.
  """
  standardValue: AdditionalTypeEnum = Field(..., description="The qualification of the Additional Type of transaction that can require the collection or delivery of initial margin when specified as a standard value.")
  """
  The qualification of the Additional Type of transaction that can require the collection or delivery of initial margin when specified as a standard value.
  """
  
  @rosetta_condition
  def condition_0_CustomValue(self):
    """
    The specification of a custom value by the parties to the legal agreement takes place alongside the qualification of the `Other` value as part of the AdditionalTypeEnum.
    """
    def _then_fn0():
      return ((self.customValue) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.standardValue, "=", AdditionalTypeEnum.OTHER), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_StandardValue(self):
    """
    The specification of a standard value by the parties to the legal agreement is done through the qualification of a value distinct than `Other` as part of the AdditionalTypeEnum, and implies that the customerValue is not being qualified.
    """
    def _then_fn0():
      return ((self.customValue) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.standardValue, "<>", AdditionalTypeEnum.OTHER), _then_fn0, _else_fn0)

from cdm.legaldocumentation.csa.AdditionalTypeEnum import AdditionalTypeEnum

AdditionalType.update_forward_refs()
