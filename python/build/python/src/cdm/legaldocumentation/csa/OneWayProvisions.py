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

__all__ = ['OneWayProvisions']


class OneWayProvisions(BaseDataClass):
  """
  A class to specify whether One Way Provisions apply in relation to the ISDA CSA for Initial Margin and, if yes, to specify the Posting Party. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles (aa): One Way Provisions.
  """
  isApplicable: bool = Field(..., description="The determination of whether the One Way Provisions are applicable (true) or not applicable (false).")
  """
  The determination of whether the One Way Provisions are applicable (true) or not applicable (false).
  """
  postingParty: Optional[CounterpartyRoleEnum] = Field(None, description="The Posting Party for the purposes of One Way Provisions. It is specified in the case where the One Way Provision is deemed applicable.")
  """
  The Posting Party for the purposes of One Way Provisions. It is specified in the case where the One Way Provision is deemed applicable.
  """
  
  @rosetta_condition
  def condition_0_PostingPartyExists(self):
    """
    A data rule to enforce that the Posting Party must be specified in the case where the One Way Provision is deemed applicable.
    """
    def _then_fn0():
      return ((self.postingParty) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_PostingPartyAbsent(self):
    """
    A data rule to enforce that the Posting Party must not be specified in the case where the One Way Provision is not deemed applicable.
    """
    def _then_fn0():
      return ((self.postingParty) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

OneWayProvisions.update_forward_refs()
