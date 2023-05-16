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

__all__ = ['EligibleCurrencyInterestRate']


class EligibleCurrencyInterestRate(BaseDataClass):
  """
  A class to specify the interest rate associated with initial margin collateral. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n): Distributions and Interest Payment (IM).
  """
  actual365Currency: AttributeWithMeta[DayCountFractionEnum] | DayCountFractionEnum = Field(..., description="")
  currency: AttributeWithMeta[str] | str = Field(..., description="The eligible currency.")
  """
  The eligible currency.
  """
  interestRate: Decimal = Field(..., description="The interest rate associated with the eligible currency.")
  """
  The interest rate associated with the eligible currency.
  """

from cdm.base.datetime.daycount.DayCountFractionEnum import DayCountFractionEnum

EligibleCurrencyInterestRate.update_forward_refs()
