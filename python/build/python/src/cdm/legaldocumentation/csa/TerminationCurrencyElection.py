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

__all__ = ['TerminationCurrencyElection']


class TerminationCurrencyElection(BaseDataClass):
  """
  A class to specify the Amendment to Termination Currency election by the parties to the agreement. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (t) (A) & (B).
  """
  currency: Optional[AttributeWithMeta[str] | str] = Field(None, description="The Termination Currency associated with the party that referenced as part of this class. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
  """
  The Termination Currency associated with the party that referenced as part of this class. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.
  """
  isSpecified: bool = Field(..., description="The qualification of whether the Termination Currency is specified in this document (True) or in an Eligible Support Credit Support (IM) Schedule (False)")
  """
  The qualification of whether the Termination Currency is specified in this document (True) or in an Eligible Support Credit Support (IM) Schedule (False)
  """
  party: List[CounterpartyRoleEnum] = Field([], description="The elective party.")
  """
  The elective party.
  """
  @rosetta_condition
  def cardinality_party(self):
    return check_cardinality(self.party, 1, 2)
  
  
  @rosetta_condition
  def condition_0_CurrencyElection(self):
    """
    A Termination Currency election should only exist when required by the affected parties election
    """
    def _then_fn0():
      return ((self.currency) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isSpecified, "=", False), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

TerminationCurrencyElection.update_forward_refs()
