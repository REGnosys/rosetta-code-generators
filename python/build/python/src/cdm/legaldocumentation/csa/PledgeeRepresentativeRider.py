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

__all__ = ['PledgeeRepresentativeRider']


class PledgeeRepresentativeRider(BaseDataClass):
  """
  The terms of the Rider for the ISDA Euroclear 2019 Collateral Transfer Agreement with respect to the use of a Pledgee Representative attached to this Agreement
  """
  isApplicable: bool = Field(..., description="Identification of whether the representative CTA provisions are applicable (True) or not applicable (False)")
  """
  Identification of whether the representative CTA provisions are applicable (True) or not applicable (False)
  """
  party: Optional[CounterpartyRoleEnum] = Field(None, description="Identification of the represented party.")
  """
  Identification of the represented party.
  """
  representativeEndDate: Optional[CustomisableOffset] = Field(None, description="The definition of representative end date in relation to a representative event.")
  """
  The definition of representative end date in relation to a representative event.
  """
  representativeEvent: Optional[ExceptionEnum] = Field(None, description="The specification of whether the representative event terms are applicable")
  """
  The specification of whether the representative event terms are applicable
  """
  representativeEventTerms: Optional[str] = Field(None, description="The specific representative event terms applicable when specified.")
  """
  The specific representative event terms applicable when specified.
  """
  representativeTerms: Optional[str] = Field(None, description="The specific representative terms applicable when specified.")
  """
  The specific representative terms applicable when specified.
  """
  
  @rosetta_condition
  def condition_0_RepresentativeParty(self):
    """
    A data rule to enforce that representative terms and a represented party are specified when representative provisions are applicable.
    """
    def _then_fn0():
      return (((((self.party) is not None) and ((self.representativeTerms) is not None)) and ((self.representativeEvent) is not None)) and ((self.representativeEndDate) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_RepresentativeEventTerms(self):
    """
    A data rule to enforce that representative event terms are specified when applicable.
    """
    def _then_fn0():
      return ((self.representativeEventTerms) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.representativeEvent, "=", ExceptionEnum.OTHER), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum
from cdm.base.datetime.CustomisableOffset import CustomisableOffset
from cdm.legaldocumentation.csa.ExceptionEnum import ExceptionEnum

PledgeeRepresentativeRider.update_forward_refs()
