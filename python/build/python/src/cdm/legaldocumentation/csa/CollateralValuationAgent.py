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

__all__ = ['CollateralValuationAgent']


class CollateralValuationAgent(BaseDataClass):
  """
  A class to specify Collateral Valuation Agent terms.
  """
  partyElection: List[CollateralValuationAgentElection] = Field([], description="The parties Collateral Valuation Agent Elections.")
  """
  The parties Collateral Valuation Agent Elections.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 0, 2)
  

from cdm.legaldocumentation.csa.CollateralValuationAgentElection import CollateralValuationAgentElection

CollateralValuationAgent.update_forward_refs()
