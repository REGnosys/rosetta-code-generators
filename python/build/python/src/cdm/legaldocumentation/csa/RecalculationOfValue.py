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

__all__ = ['RecalculationOfValue']


class RecalculationOfValue(BaseDataClass):
  """
  A class to specify terms for Recalculation of the Market Value of Posted Collateral when a dispute has been failed to be resolved by Resolution Time.
  """
  partyElection: List[RecalculationOfValueElection] = Field([], description="The parties' Recalculation of Value terms.")
  """
  The parties' Recalculation of Value terms.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 2, 2)
  

from cdm.legaldocumentation.csa.RecalculationOfValueElection import RecalculationOfValueElection

RecalculationOfValue.update_forward_refs()
