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

__all__ = ['Composite']


class Composite(BaseDataClass):
  """
  Specifies the conditions to be applied for converting into a reference currency when the actual currency rate is not determined upfront.
  """
  determinationMethod: Optional[DeterminationMethodEnum] = Field(None, description="Specifies the method according to which an amount or a date is determined.")
  """
  Specifies the method according to which an amount or a date is determined.
  """
  fixingTime: Optional[BusinessCenterTime] = Field(None, description="The time at which the spot currency exchange rate will be observed. It is specified as a time in a business day calendar location, e.g. 11:00am London time.")
  """
  The time at which the spot currency exchange rate will be observed. It is specified as a time in a business day calendar location, e.g. 11:00am London time.
  """
  fxSpotRateSource: Optional[FxSpotRateSource] = Field(None, description="Specifies the methodology (reference source and, optionally, fixing time) to be used for determining a currency conversion rate.")
  """
  Specifies the methodology (reference source and, optionally, fixing time) to be used for determining a currency conversion rate.
  """
  relativeDate: Optional[RelativeDateOffset] = Field(None, description="A date specified as some offset to another date (the anchor date).")
  """
  A date specified as some offset to another date (the anchor date).
  """

from cdm.observable.common.DeterminationMethodEnum import DeterminationMethodEnum
from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime
from cdm.observable.asset.FxSpotRateSource import FxSpotRateSource
from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset

Composite.update_forward_refs()
