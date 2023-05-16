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

__all__ = ['Quanto']


class Quanto(BaseDataClass):
  """
  Determines the currency rate that the seller of the equity amounts will apply at each valuation date for converting the respective amounts into a currency that is different from the currency denomination of the underlier.
  """
  fixingTime: Optional[BusinessCenterTime] = Field(None, description="The time at which the spot currency exchange rate will be observed. It is specified as a time in a business day calendar location, e.g. 11:00am London time.")
  """
  The time at which the spot currency exchange rate will be observed. It is specified as a time in a business day calendar location, e.g. 11:00am London time.
  """
  fxRate: List[FxRate] = Field([], description="Specifies a currency conversion rate.")
  """
  Specifies a currency conversion rate.
  """
  fxSpotRateSource: Optional[FxSpotRateSource] = Field(None, description="Specifies the methodology (reference source and, optionally, fixing time) to be used for determining a currency conversion rate.")
  """
  Specifies the methodology (reference source and, optionally, fixing time) to be used for determining a currency conversion rate.
  """

from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime
from cdm.observable.asset.FxRate import FxRate
from cdm.observable.asset.FxSpotRateSource import FxSpotRateSource

Quanto.update_forward_refs()
