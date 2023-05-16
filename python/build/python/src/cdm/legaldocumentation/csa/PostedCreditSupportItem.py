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

__all__ = ['PostedCreditSupportItem']


class PostedCreditSupportItem(BaseDataClass):
  """
  Posted Credit Support item with corresponding Valuation Percentage, FX Haircut Percentage and any related disputed Posted Credit Support valuation.
  """
  additionalHaircutPercentage: Optional[Decimal] = Field(None, description="Percentage value of any additional haircut to be applied to a collateral asset,the percentage value is expressed as the discount haircut to the value of the collateral- as an example a 5% haircut would be expressed as 0.05. ")
  """
  Percentage value of any additional haircut to be applied to a collateral asset,the percentage value is expressed as the discount haircut to the value of the collateral- as an example a 5% haircut would be expressed as 0.05. 
  """
  cashOrSecurityValue: Money = Field(..., description="The Base Currency Equivalent of Cash or Security.")
  """
  The Base Currency Equivalent of Cash or Security.
  """
  disputedCashOrSecurityValue: Money = Field(..., description="Paragraph 5. If a party (a 'Disputing Party') disputes the Value of any Posted Credit Support (IM).")
  """
  Paragraph 5. If a party (a 'Disputing Party') disputes the Value of any Posted Credit Support (IM).
  """
  fxHaircutPercentage: Optional[Decimal] = Field(None, description="FX Haircut Percentage means, for any item of Eligible Collateral (IM), the percentage specified in accordance with Paragraph 13.")
  """
  FX Haircut Percentage means, for any item of Eligible Collateral (IM), the percentage specified in accordance with Paragraph 13.
  """
  haircutPercentage: Decimal = Field(..., description="Valuation Percentage means, for any item of Eligible Collateral (IM), the percentage specified in accordance with Paragraph 13.")
  """
  Valuation Percentage means, for any item of Eligible Collateral (IM), the percentage specified in accordance with Paragraph 13.
  """

from cdm.observable.asset.Money import Money

PostedCreditSupportItem.update_forward_refs()
