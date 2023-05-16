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

__all__ = ['TradePricingReport']


class TradePricingReport(BaseDataClass):
  """
  The attributes that are specific for consensus based pricing reporting.
  """
  discountingIndex: Optional[FloatingRateIndexEnum] = Field(None, description="It specifies the interest payable on collateral delivered under a CSA covering the trade.")
  """
  It specifies the interest payable on collateral delivered under a CSA covering the trade.
  """
  pricingTime: TimeZone = Field(..., description="The regional exchange close time for the underlying contract,including time zone, at which the trades should be priced. This provides an indication for which regional snapshot should be used for pricing primarily for Global markets where there are multiple regional close times.")
  """
  The regional exchange close time for the underlying contract,including time zone, at which the trades should be priced. This provides an indication for which regional snapshot should be used for pricing primarily for Global markets where there are multiple regional close times.
  """
  trade: Trade = Field(..., description="Represents the cosensus based pricing parameters on a trade basis.")
  """
  Represents the cosensus based pricing parameters on a trade basis.
  """

from cdm.base.staticdata.asset.rates.FloatingRateIndexEnum import FloatingRateIndexEnum
from cdm.base.datetime.TimeZone import TimeZone
from cdm.event.common.Trade import Trade

TradePricingReport.update_forward_refs()
