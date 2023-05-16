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

__all__ = ['CollateralValuationAgentElection']


class CollateralValuationAgentElection(BaseDataClass):
  """
  A class to specify Collateral Valuation Agent language.
  """
  additionalLanguage: Optional[str] = Field(None, description="The additional language that might be specified by the parties to the legal agreement.")
  """
  The additional language that might be specified by the parties to the legal agreement.
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

CollateralValuationAgentElection.update_forward_refs()
