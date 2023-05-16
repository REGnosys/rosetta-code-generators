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

__all__ = ['HoldingAndUsingPostedCollateral']


class HoldingAndUsingPostedCollateral(BaseDataClass):
  """
  A class to specify the elections for the holding and using of posted collateral by the respective parties to the Credit Support Annex for Variation Margin. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (h): Holding and Using Posted Collateral (VM).
  """
  partyElection: List[HoldingAndUsingPostedCollateralElection] = Field([], description="The parties' elections for the holding and using of posted collateral.")
  """
  The parties' elections for the holding and using of posted collateral.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 2, 2)
  

from cdm.legaldocumentation.csa.HoldingAndUsingPostedCollateralElection import HoldingAndUsingPostedCollateralElection

HoldingAndUsingPostedCollateral.update_forward_refs()
