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

__all__ = ['PostingObligationsElection']


class PostingObligationsElection(BaseDataClass):
  """
  A class to specify the collateral posting obligations for the security provider party(ies), for example, as specified under the terms of the ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (ii).
  """
  additionalLanguage: Optional[str] = Field(None, description="The additional language that might be specified by the parties to the legal agreement.")
  """
  The additional language that might be specified by the parties to the legal agreement.
  """
  asPermitted: bool = Field(..., description="If set to True, the Control Agreement is a Credit Support Document with respect to the party(ies). ISDA 2016 Credit Support Annex for Initial Margin, paragraph 6, (e).")
  """
  If set to True, the Control Agreement is a Credit Support Document with respect to the party(ies). ISDA 2016 Credit Support Annex for Initial Margin, paragraph 6, (e).
  """
  eligibleCollateral: List[EligibleCollateralSchedule] = Field([], description="The eligible collateral as specified in relation to the pledgor/chargor/obligor(s) posting obligation. ISDA 2016 Credit Support Annex for Initial Margin, Eligible Credit Support (IM) Schedule.")
  """
  The eligible collateral as specified in relation to the pledgor/chargor/obligor(s) posting obligation. ISDA 2016 Credit Support Annex for Initial Margin, Eligible Credit Support (IM) Schedule.
  """
  excludedCollateral: Optional[str] = Field(None, description="The excluded collateral as specified in relation to the pledgor/chargor/obligor(s) posting obligation. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (ii)(B)(i).")
  """
  The excluded collateral as specified in relation to the pledgor/chargor/obligor(s) posting obligation. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (ii)(B)(i).
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  
  @rosetta_condition
  def condition_0_AsPermitted(self):
    """
    A data rule to enforce that the eligible collateral should be specified when the Control Agreement is a Credit Support Document with respect to the party(ies).
    """
    def _then_fn0():
      return ((self.eligibleCollateral) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.asPermitted, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_EligibleCollateral(self):
    """
    A data rule to enforce that the eligible collateral shouldn't be specified when the Control Agreement isn't deemed a Credit Support Document with respect to the party(ies).
    """
    def _then_fn0():
      return ((self.eligibleCollateral) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.asPermitted, "=", False), _then_fn0, _else_fn0)

from cdm.legaldocumentation.csa.EligibleCollateralSchedule import EligibleCollateralSchedule
from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

PostingObligationsElection.update_forward_refs()
