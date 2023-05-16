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

__all__ = ['TerminationCurrencyAmendment']


class TerminationCurrencyAmendment(BaseDataClass):
  """
  A class to specify the Amendment to Termination Currency elections by the parties to the agreement. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (t): Amendment to Termination Currency.
  """
  effectiveDate: Optional[AmendmentEffectiveDate] = Field(None, description="The effective date of the Amendment to Termination Currency. This date can be specified as either an actual date, a specific date (e.g. the annex date) or as a custom provision.")
  """
  The effective date of the Amendment to Termination Currency. This date can be specified as either an actual date, a specific date (e.g. the annex date) or as a custom provision.
  """
  isApplicable: bool = Field(..., description="The qualification of whether the Amendment to Termination Currency is deemed applicable by the parties (True) or not (False).")
  """
  The qualification of whether the Amendment to Termination Currency is deemed applicable by the parties (True) or not (False).
  """
  partyElection: List[TerminationCurrencyElection] = Field([], description="The parties' Amendment Currency election.")
  """
  The parties' Amendment Currency election.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 0, 3)
  
  
  @rosetta_condition
  def condition_0_Applicability(self):
    """
    The Amendment to Termination Currency elections only apply when the Amendment to Termination Currency is deemed applicable by the parties.
    """
    def _then_fn0():
      return (((self.effectiveDate) is None) and ((self.partyElection) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isApplicable, "=", False), _then_fn0, _else_fn0)

from cdm.legaldocumentation.csa.AmendmentEffectiveDate import AmendmentEffectiveDate
from cdm.legaldocumentation.csa.TerminationCurrencyElection import TerminationCurrencyElection

TerminationCurrencyAmendment.update_forward_refs()
