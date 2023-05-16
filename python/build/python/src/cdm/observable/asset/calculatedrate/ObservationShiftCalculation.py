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

__all__ = ['ObservationShiftCalculation']


class ObservationShiftCalculation(BaseDataClass):
  """
  Parameters to describe the observation shift for a daily compounded or averaged floating rate. This type is used to represent modular computed rates in interestRatePayouts.
  """
  additionalBusinessDays: Optional[BusinessCenters] = Field(None, description="Any additional business days that be applicable.")
  """
  Any additional business days that be applicable.
  """
  calculationBase: Optional[ObservationPeriodDatesEnum] = Field(None, description="Whether the rate is calculated in advance, in arrears, or relative to a reset date.")
  """
  Whether the rate is calculated in advance, in arrears, or relative to a reset date.
  """
  offsetDays: Optional[int] = Field(None, description="The number of days of observation shift.")
  """
  The number of days of observation shift.
  """

from cdm.base.datetime.BusinessCenters import BusinessCenters
from cdm.observable.asset.calculatedrate.ObservationPeriodDatesEnum import ObservationPeriodDatesEnum

ObservationShiftCalculation.update_forward_refs()
