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

__all__ = ['DividendTerms']


class DividendTerms(BaseDataClass):
  """
  Information related to dividends and payments.
  """
  dividendEntitlement: Optional[DividendEntitlementEnum] = Field(None, description="Defines the date on which the receiver of the equity return is entitled to the dividend.")
  """
  Defines the date on which the receiver of the equity return is entitled to the dividend.
  """
  manufacturedIncomeRequirement: DividendPayoutRatio = Field(..., description="Specifies the proportion of the value of the dividend on the borrowed shares that the borrower is legally obligated to return to the lender.")
  """
  Specifies the proportion of the value of the dividend on the borrowed shares that the borrower is legally obligated to return to the lender.
  """
  minimumBillingAmount: Optional[Money] = Field(None, description="daily fee increments accrue until a threshold is crossed, at which point payment becomes due)")
  """
  daily fee increments accrue until a threshold is crossed, at which point payment becomes due)
  """

from cdm.product.asset.DividendEntitlementEnum import DividendEntitlementEnum
from cdm.product.asset.DividendPayoutRatio import DividendPayoutRatio
from cdm.observable.asset.Money import Money

DividendTerms.update_forward_refs()
