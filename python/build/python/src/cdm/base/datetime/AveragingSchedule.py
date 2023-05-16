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

__all__ = ['AveragingSchedule']


class AveragingSchedule(BaseDataClass):
  """
  Class to representing a method for generating a series of dates.
  """
  averagingPeriodFrequency: CalculationPeriodFrequency = Field(..., description="The frequency at which averaging period occurs with the regular part of the valuation schedule and their roll date convention.")
  """
  The frequency at which averaging period occurs with the regular part of the valuation schedule and their roll date convention.
  """
  endDate: date = Field(..., description="Date on which this period ends.")
  """
  Date on which this period ends.
  """
  startDate: date = Field(..., description="Date on which this period begins.")
  """
  Date on which this period begins.
  """

from cdm.base.datetime.CalculationPeriodFrequency import CalculationPeriodFrequency

AveragingSchedule.update_forward_refs()
