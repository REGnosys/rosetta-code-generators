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

__all__ = ['CollateralManagementAgreementElection']


class CollateralManagementAgreementElection(BaseDataClass):
  """
  A class to specify the Collateral Management Agreement election by each party as the Obligee. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (b(i): Collateral Management Agreement.
  """
  collateralManagementAgreement: str = Field(..., description="The designated Collateral Management Agreement with respect to the elective party as the Obligee.")
  """
  The designated Collateral Management Agreement with respect to the elective party as the Obligee.
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

CollateralManagementAgreementElection.update_forward_refs()
