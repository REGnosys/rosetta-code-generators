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

__all__ = ['TerminationCurrencySelection']


class TerminationCurrencySelection(BaseDataClass):
  """
  Specifies Termination Currency where a currency is stated at the time the agreement is entered into.
  """
  bothAffected: Optional[str] = Field(None, description="Specifies fallback Termination Currency where both parties are Affected Parties.")
  """
  Specifies fallback Termination Currency where both parties are Affected Parties.
  """
  fallbackCurrency: Optional[str] = Field(None, description="Specifies a single fallback Termination Currency should the stated currency not be freely available.")
  """
  Specifies a single fallback Termination Currency should the stated currency not be freely available.
  """
  partyElection: List[PartyTerminationCurrencySelection] = Field([], description="Specifies different termination currencies to apply depending on which party or parties are the Defaulting Party Affected Party(ies).")
  """
  Specifies different termination currencies to apply depending on which party or parties are the Defaulting Party Affected Party(ies).
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 0, 2)
  
  statedCurrency: Optional[str] = Field(None, description="Specifies a single Termination Currency for the agreement.")
  """
  Specifies a single Termination Currency for the agreement.
  """

from cdm.legaldocumentation.master.PartyTerminationCurrencySelection import PartyTerminationCurrencySelection

TerminationCurrencySelection.update_forward_refs()
