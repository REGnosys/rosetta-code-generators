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

__all__ = ['FloatingRateIndexCalculationDefaults']


class FloatingRateIndexCalculationDefaults(BaseDataClass):
  """
  This holds the rate calculation defaults applicable for a floating rate index.
  """
  applicableBusinessDays: Optional[BusinessCenters] = Field(None, description="The default applicable business days.")
  """
  The default applicable business days.
  """
  category: Optional[FloatingRateIndexCategoryEnum] = Field(None, description="The ISDA FRO category (e.g. screen rate or calculated rate).")
  """
  The ISDA FRO category (e.g. screen rate or calculated rate).
  """
  dayCountFraction: Optional[DayCountFractionEnum] = Field(None, description="The default day count fraction.")
  """
  The default day count fraction.
  """
  fixing: List[FloatingRateIndexFixingDetails] = Field([], description="The default fixing details.")
  """
  The default fixing details.
  """
  indexStyle: Optional[FloatingRateIndexStyleEnum] = Field(None, description="The ISDA FRO style (e.g. term rate, swap rate, etc).")
  """
  The ISDA FRO style (e.g. term rate, swap rate, etc).
  """
  method: Optional[FloatingRateIndexCalculationMethodEnum] = Field(None, description="The ISDA FRO calculation method (e.g. OIS Compounding).")
  """
  The ISDA FRO calculation method (e.g. OIS Compounding).
  """
  publicationCalendar: Optional[BusinessCenterEnum] = Field(None, description="Publication Calendar (e.g. EUR-ICESWAP)")
  """
  Publication Calendar (e.g. EUR-ICESWAP)
  """

from cdm.base.datetime.BusinessCenters import BusinessCenters
from cdm.observable.asset.fro.FloatingRateIndexCategoryEnum import FloatingRateIndexCategoryEnum
from cdm.base.datetime.daycount.DayCountFractionEnum import DayCountFractionEnum
from cdm.observable.asset.fro.FloatingRateIndexFixingDetails import FloatingRateIndexFixingDetails
from cdm.observable.asset.fro.FloatingRateIndexStyleEnum import FloatingRateIndexStyleEnum
from cdm.observable.asset.fro.FloatingRateIndexCalculationMethodEnum import FloatingRateIndexCalculationMethodEnum
from cdm.base.datetime.BusinessCenterEnum import BusinessCenterEnum

FloatingRateIndexCalculationDefaults.update_forward_refs()
