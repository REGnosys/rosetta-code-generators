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

__all__ = ['MarginCallIssuance']

from cdm.event.common.MarginCallBase import MarginCallBase

class MarginCallIssuance(MarginCallBase):
  """
  Represents common attributes required for a Margin Call Issuance under a legal agreement such as a credit support document or equivalent.
  """
  callAmountInBaseCurrency: Money = Field(..., description="Specifies the amount of margin being called for which accounts for margin calculation inclusive of exposure, independent amount,threshold,collateral balance, MTA, rounding increments (in base currency detailed in supporting collateral agreement).")
  """
  Specifies the amount of margin being called for which accounts for margin calculation inclusive of exposure, independent amount,threshold,collateral balance, MTA, rounding increments (in base currency detailed in supporting collateral agreement).
  """
  recallNonCashCollateralDescription: List[EligibleCollateralCriteria] = Field([], description="Specifies the details to describe or identify non-cash collateral eligible assets for recall purposes.")
  """
  Specifies the details to describe or identify non-cash collateral eligible assets for recall purposes.
  """

from cdm.observable.asset.Money import Money
from cdm.legaldocumentation.csa.EligibleCollateralCriteria import EligibleCollateralCriteria

MarginCallIssuance.update_forward_refs()
