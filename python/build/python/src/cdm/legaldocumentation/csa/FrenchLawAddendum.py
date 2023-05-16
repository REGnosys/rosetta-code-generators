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

__all__ = ['FrenchLawAddendum']


class FrenchLawAddendum(BaseDataClass):
  """
  A class to specify party specific elections when a Collateral Transfer Agreement is governed by French Law.
  """
  isApplicable: bool = Field(..., description="The qualification of whether the French Law Addendum is deemed applicable by the parties (True) or not (False).")
  """
  The qualification of whether the French Law Addendum is deemed applicable by the parties (True) or not (False).
  """
  partyElection: List[FrenchLawAddendumElection] = Field([], description="The parties French Law Addendum Elections.")
  """
  The parties French Law Addendum Elections.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 0, 2)
  
  
  @rosetta_condition
  def condition_0_Applicable(self):
    """
    A data rule to enforce that the French Law Addendum party elections must be specified when applicable.
    """
    def _then_fn0():
      return all_elements(len(self.partyElection), "=", 2)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)

from cdm.legaldocumentation.csa.FrenchLawAddendumElection import FrenchLawAddendumElection

FrenchLawAddendum.update_forward_refs()
