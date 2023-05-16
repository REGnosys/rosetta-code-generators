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

__all__ = ['PerformanceValuationDates']


class PerformanceValuationDates(BaseDataClass):
  """
  Defines how and when a performance type option or performance type swap is to be valued.
  """
  determinationMethod: DeterminationMethodEnum = Field(..., description="Specifies the method according to which an amount or a date is determined.")
  """
  Specifies the method according to which an amount or a date is determined.
  """
  valuationDate: Optional[AdjustableOrRelativeDate] = Field(None, description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Pricing Date")
  """
  2018 ISDA CDM Equity Confirmation for Security Equity Swap: Pricing Date
  """
  valuationDates: Optional[AdjustableRelativeOrPeriodicDates] = Field(None, description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Pricing Date")
  """
  2018 ISDA CDM Equity Confirmation for Security Equity Swap: Pricing Date
  """
  valuationTime: Optional[BusinessCenterTime] = Field(None, description="The specific time of day at which the calculation agent values the underlying. The SpecificTime is the only case when the valuationTime (time + business center location  e.g. 10:00:00 USNY) should be provided. You should be able to provide just the valuationTime without valuationTimeType, which infer that this is a specific time.")
  """
  The specific time of day at which the calculation agent values the underlying. The SpecificTime is the only case when the valuationTime (time + business center location  e.g. 10:00:00 USNY) should be provided. You should be able to provide just the valuationTime without valuationTimeType, which infer that this is a specific time.
  """
  valuationTimeType: Optional[TimeTypeEnum] = Field(None, description="The time of day at which the calculation agent values the underlying, for example the official closing time of the exchange.")
  """
  The time of day at which the calculation agent values the underlying, for example the official closing time of the exchange.
  """

from cdm.observable.common.DeterminationMethodEnum import DeterminationMethodEnum
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.base.datetime.AdjustableRelativeOrPeriodicDates import AdjustableRelativeOrPeriodicDates
from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime
from cdm.observable.common.TimeTypeEnum import TimeTypeEnum

PerformanceValuationDates.update_forward_refs()
