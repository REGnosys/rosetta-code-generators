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

__all__ = ['SwapCurveValuation']


class SwapCurveValuation(BaseDataClass):
  """
  A class to specify a valuation swap curve, which is used as part of the strike construct for the bond and convertible bond options.
  """
  floatingRateIndex: FloatingRateIndexEnum = Field(..., description="")
  indexTenor: Optional[Period] = Field(None, description="The ISDA Designated Maturity, i.e. the tenor of the floating rate.")
  """
  The ISDA Designated Maturity, i.e. the tenor of the floating rate.
  """
  side: Optional[QuotationSideEnum] = Field(None, description="The side (bid/mid/ask) of the measure.")
  """
  The side (bid/mid/ask) of the measure.
  """
  spread: Decimal = Field(..., description="Spread in basis points over the floating rate index.")
  """
  Spread in basis points over the floating rate index.
  """

from cdm.base.staticdata.asset.rates.FloatingRateIndexEnum import FloatingRateIndexEnum
from cdm.base.datetime.Period import Period
from cdm.observable.asset.QuotationSideEnum import QuotationSideEnum

SwapCurveValuation.update_forward_refs()
