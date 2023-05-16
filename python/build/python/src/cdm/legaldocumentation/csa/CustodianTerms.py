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

__all__ = ['CustodianTerms']


class CustodianTerms(BaseDataClass):
  """
  A class to specify the requirements applicable to the custodian with respect to the holding of posted collateral. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (h)(i): Eligibility to Hold Posted Collateral (VM) Custodians (VM).
  """
  initialDesignation: Optional[LegalEntity] = Field(None, description="The 2016 ISDA CSA for Variation Margin provides the ability for the parties to specify the initial custodian.")
  """
  The 2016 ISDA CSA for Variation Margin provides the ability for the parties to specify the initial custodian.
  """
  minimumAssets: Optional[Money] = Field(None, description="The minimal level of assets requirement with respect to the custody agent.")
  """
  The minimal level of assets requirement with respect to the custody agent.
  """
  minimumRating: Optional[CreditNotation] = Field(None, description="The minimal rating requirement with respect to the custody agent.")
  """
  The minimal rating requirement with respect to the custody agent.
  """

from cdm.base.staticdata.party.LegalEntity import LegalEntity
from cdm.observable.asset.Money import Money
from cdm.observable.asset.CreditNotation import CreditNotation

CustodianTerms.update_forward_refs()
