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

__all__ = ['PriceReturnTerms']


class PriceReturnTerms(BaseDataClass):
  conversionFactor: Optional[Decimal] = Field(None, description="Defines the conversion applied if the quantity unit on contract is different from unit on referenced underlier.")
  """
  Defines the conversion applied if the quantity unit on contract is different from unit on referenced underlier.
  """
  performance: Optional[str] = Field(None, description="Performance calculation, in accordance with Part 1 Section 12 of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap, Para 75. 'Equity Performance'. Cumulative performance is used as a notional multiplier factor on both legs of an Equity Swap.")
  """
  Performance calculation, in accordance with Part 1 Section 12 of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap, Para 75. 'Equity Performance'. Cumulative performance is used as a notional multiplier factor on both legs of an Equity Swap.
  """
  returnType: ReturnTypeEnum = Field(..., description="The type of return associated with the equity swap.")
  """
  The type of return associated with the equity swap.
  """
  valuationPriceFinal: Optional[PriceSchedule] = Field(None, description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Final Price | Specifies the final valuation price of the underlier. This price can be expressed either as an actual amount/currency, as a determination method, or by reference to another value specified in the swap document.")
  """
  2018 ISDA CDM Equity Confirmation for Security Equity Swap: Final Price | Specifies the final valuation price of the underlier. This price can be expressed either as an actual amount/currency, as a determination method, or by reference to another value specified in the swap document.
  """
  valuationPriceInitial: Optional[PriceSchedule] = Field(None, description="Specifies the initial valuation price(s) of the underlier. This price can be expressed either as an actual amount/currency, as a determination method, or by reference to another value specified in the swap document.")
  """
  Specifies the initial valuation price(s) of the underlier. This price can be expressed either as an actual amount/currency, as a determination method, or by reference to another value specified in the swap document.
  """

from cdm.product.asset.ReturnTypeEnum import ReturnTypeEnum
from cdm.observable.asset.PriceSchedule import PriceSchedule

PriceReturnTerms.update_forward_refs()
