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

__all__ = ['PartyTerminationCurrencySelection']


class PartyTerminationCurrencySelection(BaseDataClass):
  """
  Specifies the termination currency to be used by a party when it is the Non-Defaulting Party or the Party which is not the Affected Party.
  """
  party: Party = Field(..., description="The elective party.")
  """
  The elective party.
  """
  statedPartyCurrency: str = Field(..., description="Specifies termination Currency")
  """
  Specifies termination Currency
  """

from cdm.base.staticdata.party.Party import Party

PartyTerminationCurrencySelection.update_forward_refs()
