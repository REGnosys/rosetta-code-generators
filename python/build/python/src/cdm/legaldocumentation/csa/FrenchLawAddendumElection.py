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

__all__ = ['FrenchLawAddendumElection']


class FrenchLawAddendumElection(BaseDataClass):
  """
  A class to specify party specific French Law Addendum language
  """
  addendumLanguage: Optional[str] = Field(None, description="The party specific language to be included in the agreement.")
  """
  The party specific language to be included in the agreement.
  """
  isApplicable: bool = Field(..., description="The qualification of whether the party elects specific language")
  """
  The qualification of whether the party elects specific language
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  
  @rosetta_condition
  def condition_0_AddendumLanguage(self):
    """
    A data rule to enforce that the French Law Addendum party language must be specified when applicable.
    """
    def _then_fn1():
      return ((self.addendumLanguage) is None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return ((self.addendumLanguage) is not None)
    
    def _else_fn0():
      return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn1, _else_fn1)
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

FrenchLawAddendumElection.update_forward_refs()
