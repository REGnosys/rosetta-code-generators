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

__all__ = ['RecalculationOfValueElection']


class RecalculationOfValueElection(BaseDataClass):
  """
  A class to specify Recalculation of Value terms that will be applicable
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  recalculationOfValueElection: RecalculationOfValueElectionEnum = Field(..., description="The procedure for Recalculation of Value.")
  """
  The procedure for Recalculation of Value.
  """
  recalculationOfValueTerms: Optional[str] = Field(None, description="Additional Recalculation of Value terms when specified")
  """
  Additional Recalculation of Value terms when specified
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum
from cdm.legaldocumentation.csa.RecalculationOfValueElectionEnum import RecalculationOfValueElectionEnum

RecalculationOfValueElection.update_forward_refs()
