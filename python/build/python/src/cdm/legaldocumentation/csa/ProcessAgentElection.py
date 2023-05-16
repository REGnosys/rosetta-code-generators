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

__all__ = ['ProcessAgentElection']


class ProcessAgentElection(BaseDataClass):
  """
  A class to specify the parties' respective elections with respect to the Process Agent.
  """
  isApplicable: bool = Field(..., description="The qualification of whether the Process Agent is applicable (True) or not applicable (False).")
  """
  The qualification of whether the Process Agent is applicable (True) or not applicable (False).
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  processAgent: Optional[PartyContactInformation] = Field(None, description="The Process Agent specification, when applicable.")
  """
  The Process Agent specification, when applicable.
  """
  
  @rosetta_condition
  def condition_0_Applicable(self):
    """
    A data rule to enforce that the Process Agent must be specified when it is applicable.
    """
    def _then_fn0():
      return ((self.processAgent) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_NotApplicable(self):
    """
    A data rule to enforce that the Process Agent cannot be specified if deemed not applicable.
    """
    def _then_fn0():
      return ((self.processAgent) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum
from cdm.base.staticdata.party.PartyContactInformation import PartyContactInformation

ProcessAgentElection.update_forward_refs()
