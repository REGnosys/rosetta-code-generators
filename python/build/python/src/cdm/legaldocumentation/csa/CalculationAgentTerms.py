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

__all__ = ['CalculationAgentTerms']


class CalculationAgentTerms(BaseDataClass):
  """
  A class to specify Calculation Agent for purposes of Initial or Variation Margin agreements
  """
  bespokeCalculationAgentTerms: Optional[str] = Field(None, description="The Calculation Agent (IM) terms when specified")
  """
  The Calculation Agent (IM) terms when specified
  """
  party: List[CounterpartyRoleEnum] = Field([], description="The party which is specified as Calculation Agent for Initial Margin.")
  """
  The party which is specified as Calculation Agent for Initial Margin.
  """
  @rosetta_condition
  def cardinality_party(self):
    return check_cardinality(self.party, 0, 2)
  
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('party', 'bespokeCalculationAgentTerms', necessity=True)

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

CalculationAgentTerms.update_forward_refs()
