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

__all__ = ['SimmCalculationCurrency']


class SimmCalculationCurrency(BaseDataClass):
  """
  A class to specify the SIMM Calculation Currency elections by each party to the agreement.
  """
  partyElection: List[CalculationCurrencyElection] = Field([], description="The parties' SIMM Calculation Currency election.")
  """
  The parties' SIMM Calculation Currency election.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 2, 2)
  

from cdm.legaldocumentation.csa.CalculationCurrencyElection import CalculationCurrencyElection

SimmCalculationCurrency.update_forward_refs()
