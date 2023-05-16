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

__all__ = ['UmbrellaAgreement']


class UmbrellaAgreement(BaseDataClass):
  """
  A class to specify a set of legal entities which are part of a legal agreement beyond the two contracting parties to that agreement. This data representation reflects the ISDA Create representation.
  """
  isApplicable: bool = Field(..., description="The determination of whether Umbrella Agreement terms are Applicable (True), or Not Applicable (False)")
  """
  The determination of whether Umbrella Agreement terms are Applicable (True), or Not Applicable (False)
  """
  language: Optional[str] = Field(None, description="The language associated with the umbrella agreement, and which applies to all the parties to the umbrella agreement.")
  """
  The language associated with the umbrella agreement, and which applies to all the parties to the umbrella agreement.
  """
  parties: List[UmbrellaAgreementEntity] = Field([], description="Underlying principals to the umbrella agreement.")
  """
  Underlying principals to the umbrella agreement.
  """
  
  @rosetta_condition
  def condition_0_UmbrellaAgreementExists(self):
    """
    Umbrella Agreement language and parties should not exist when Umbrella Agreement terms are Not Applicable.
    """
    def _then_fn0():
      return (((self.language) is not None) and ((self.parties) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)

from cdm.legaldocumentation.common.UmbrellaAgreementEntity import UmbrellaAgreementEntity

UmbrellaAgreement.update_forward_refs()
