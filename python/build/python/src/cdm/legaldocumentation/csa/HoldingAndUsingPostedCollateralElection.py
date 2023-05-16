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

__all__ = ['HoldingAndUsingPostedCollateralElection']


class HoldingAndUsingPostedCollateralElection(BaseDataClass):
  """
  A class to specify the parties' elections related to the holding and using of posted collateral. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (h): Holding and Using Posted Collateral (VM).
  """
  eligibilityToHoldCollateral: EligibilityToHoldCollateral = Field(..., description="The specification of the conditions under which a party and its custodian(s) are entitled to hold posted collateral.")
  """
  The specification of the conditions under which a party and its custodian(s) are entitled to hold posted collateral.
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  useOfPostedCollateral: bool = Field(..., description="Specifies whether the party to the agreement has the right to rehypothecate the collateral held (True), i.e. whether the condition specified in Paragraph 6, (c) of the ISDA 2016 Credit Support Annex for Variation Margin apply. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (h)(ii): Use of Posted Collateral (VM).")
  """
  Specifies whether the party to the agreement has the right to rehypothecate the collateral held (True), i.e. whether the condition specified in Paragraph 6, (c) of the ISDA 2016 Credit Support Annex for Variation Margin apply. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (h)(ii): Use of Posted Collateral (VM).
  """

from cdm.legaldocumentation.csa.EligibilityToHoldCollateral import EligibilityToHoldCollateral
from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

HoldingAndUsingPostedCollateralElection.update_forward_refs()
