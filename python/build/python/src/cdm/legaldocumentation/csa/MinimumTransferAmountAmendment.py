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

__all__ = ['MinimumTransferAmountAmendment']


class MinimumTransferAmountAmendment(BaseDataClass):
  """
   A class to specify whether Amendment to Minimum Transfer Amount language is applicable or not
  """
  effectiveDate: Optional[AmendmentEffectiveDate] = Field(None, description="The effective date of the Amendment to Termination Currency.")
  """
  The effective date of the Amendment to Termination Currency.
  """
  isApplicable: bool = Field(..., description="The definition of Minimum Transfer Amount in any Other Regulatory CSA will be amended when applicable.")
  """
  The definition of Minimum Transfer Amount in any Other Regulatory CSA will be amended when applicable.
  """
  partyElections: List[ElectiveAmountElection] = Field([], description="The party elective amounts.")
  """
  The party elective amounts.
  """
  @rosetta_condition
  def cardinality_partyElections(self):
    return check_cardinality(self.partyElections, 0, 2)
  
  
  @rosetta_condition
  def condition_0_AmendmentNotApplicable(self):
    """
    A data rule to enforce that the Effective Date and Party Elections should be absent when the Minimum Transfer Amount Amendment is stated as not specified for the                       agreement.
    """
    def _then_fn0():
      return (((self.effectiveDate) is None) and ((self.partyElections) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)

from cdm.legaldocumentation.csa.AmendmentEffectiveDate import AmendmentEffectiveDate
from cdm.legaldocumentation.csa.ElectiveAmountElection import ElectiveAmountElection

MinimumTransferAmountAmendment.update_forward_refs()
