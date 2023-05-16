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

__all__ = ['ObservationDates']


class ObservationDates(BaseDataClass):
  """
  Describes date details for a set of observation dates in parametric or non-parametric form.
  """
  observationSchedule: List[ObservationSchedule] = Field([], description="Specifies a schedule of dates (non-parametric) on which market observations take place, and allows for the optional definition of weights where applicable.  When no weight is specified, then weight of each date is assumed to be 1.0")
  """
  Specifies a schedule of dates (non-parametric) on which market observations take place, and allows for the optional definition of weights where applicable.  When no weight is specified, then weight of each date is assumed to be 1.0
  """
  parametricDates: Optional[ParametricDates] = Field(None, description="Specifies parametric terms to determine which days within a given calculation period the price would be observed. Typically associated with Commodities. ")
  """
  Specifies parametric terms to determine which days within a given calculation period the price would be observed. Typically associated with Commodities. 
  """
  periodicSchedule: Optional[PeriodicDates] = Field(None, description="Specifies the date range and frequency on which market observations take place.  Weights can be assigned to dates in the schedule by assigning the weight and corresponding observationReference in the observationSchedule.")
  """
  Specifies the date range and frequency on which market observations take place.  Weights can be assigned to dates in the schedule by assigning the weight and corresponding observationReference in the observationSchedule.
  """

from cdm.product.common.schedule.ObservationSchedule import ObservationSchedule
from cdm.product.common.schedule.ParametricDates import ParametricDates
from cdm.base.datetime.PeriodicDates import PeriodicDates

ObservationDates.update_forward_refs()
