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

__all__ = ['TerminationCurrency']


class TerminationCurrency(BaseDataClass):
  """
  Specifies how the Termination Currency for the agreement will be determined.
  """
  partyOptionTerminationCurrency: Optional[PartyOptionTerminationCurrency] = Field(None, description="Provides that the Termination Currency will be determined by reference to a contractual mechanism when closing out the Agreement.")
  """
  Provides that the Termination Currency will be determined by reference to a contractual mechanism when closing out the Agreement.
  """
  statedTerminationCurrency: Optional[TerminationCurrencySelection] = Field(None, description="Allows for specific Termination Currency(ies) and a fallback Termination Currency to be selected.")
  """
  Allows for specific Termination Currency(ies) and a fallback Termination Currency to be selected.
  """

from cdm.legaldocumentation.master.PartyOptionTerminationCurrency import PartyOptionTerminationCurrency
from cdm.legaldocumentation.master.TerminationCurrencySelection import TerminationCurrencySelection

TerminationCurrency.update_forward_refs()
