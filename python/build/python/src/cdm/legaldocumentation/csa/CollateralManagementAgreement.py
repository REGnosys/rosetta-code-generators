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

__all__ = ['CollateralManagementAgreement']


class CollateralManagementAgreement(BaseDataClass):
  """
  A class to specify the Collateral Management Agreement election by the respective parties to a Japanese Law ISDA CSA. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (b)(i): Collateral Management Agreement.
  """
  partyElection: List[CollateralManagementAgreementElection] = Field([], description="The parties' Collateral Management Agreement election.")
  """
  The parties' Collateral Management Agreement election.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 2, 2)
  

from cdm.legaldocumentation.csa.CollateralManagementAgreementElection import CollateralManagementAgreementElection

CollateralManagementAgreement.update_forward_refs()
