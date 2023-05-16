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

__all__ = ['PeriodicDates']


class PeriodicDates(BaseDataClass):
  """
  A class for specifying a calculation period schedule.
  """
  dayType: Optional[DayTypeEnum] = Field(None, description="Denotes the enumerated values to specify the day type classification used in counting the number of days between two dates.")
  """
  Denotes the enumerated values to specify the day type classification used in counting the number of days between two dates.
  """
  endDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The end date of the calculation period. FpML specifies that for interest rate swaps this date must only be specified if it is not equal to the termination date. It is always specified in the case of equity swaps with periodic payments. This date may be subject to adjustment in accordance with a business day convention.")
  """
  The end date of the calculation period. FpML specifies that for interest rate swaps this date must only be specified if it is not equal to the termination date. It is always specified in the case of equity swaps with periodic payments. This date may be subject to adjustment in accordance with a business day convention.
  """
  periodDatesAdjustments: Optional[BusinessDayAdjustments] = Field(None, description="The specification of the business day convention and financial business centers used for adjusting any calculation period date if it would otherwise fall on a day that is not a business day in the specified business center.")
  """
  The specification of the business day convention and financial business centers used for adjusting any calculation period date if it would otherwise fall on a day that is not a business day in the specified business center.
  """
  periodFrequency: Optional[CalculationPeriodFrequency] = Field(None, description="The frequency at which calculation period end dates occur with the regular part of the calculation period schedule and their roll date convention.")
  """
  The frequency at which calculation period end dates occur with the regular part of the calculation period schedule and their roll date convention.
  """
  startDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The start date of the calculation period. FpML specifies that for interest rate swaps this date must only be specified if it is not equal to the effective date. It is always specified in the case of equity swaps and credit default swaps with periodic payments. This date may be subject to adjustment in accordance with a business day convention.")
  """
  The start date of the calculation period. FpML specifies that for interest rate swaps this date must only be specified if it is not equal to the effective date. It is always specified in the case of equity swaps and credit default swaps with periodic payments. This date may be subject to adjustment in accordance with a business day convention.
  """

from cdm.base.datetime.DayTypeEnum import DayTypeEnum
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments
from cdm.base.datetime.CalculationPeriodFrequency import CalculationPeriodFrequency

PeriodicDates.update_forward_refs()
