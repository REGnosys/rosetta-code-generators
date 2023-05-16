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

__all__ = ['EligibilityToHoldCollateral']


class EligibilityToHoldCollateral(BaseDataClass):
  """
  A class to specify the conditions under which a party and its custodian(s) are entitled to hold collateral. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (h)(i): Eligibility to Hold Posted Collateral (VM) Custodians (VM).
  """
  custodianTerms: Optional[CustodianTerms] = Field(None, description="The restrictions that might be required by a party from the other party's custodian agent to hold its posted collateral.")
  """
  The restrictions that might be required by a party from the other party's custodian agent to hold its posted collateral.
  """
  eligibleCountry: List[AttributeWithMeta[str] | str] = Field([], description="The restrictions that might be required by a party from the other party in terms of country(ies) where collateral can be held.")
  """
  The restrictions that might be required by a party from the other party in terms of country(ies) where collateral can be held.
  """
  partyTerms: List[HoldingPostedCollateralEnum] = Field([], description="The condition(s) required by a party from the other party to hold its posted collateral.")
  """
  The condition(s) required by a party from the other party to hold its posted collateral.
  """
  @rosetta_condition
  def cardinality_partyTerms(self):
    return check_cardinality(self.partyTerms, 1, None)
  

from cdm.legaldocumentation.csa.CustodianTerms import CustodianTerms
from cdm.legaldocumentation.csa.HoldingPostedCollateralEnum import HoldingPostedCollateralEnum

EligibilityToHoldCollateral.update_forward_refs()
