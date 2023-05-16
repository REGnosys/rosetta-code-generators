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

__all__ = ['AveragingPeriod']


class AveragingPeriod(BaseDataClass):
  """
  Period over which an average value is taken.
  """
  averagingDateTimes: Optional[DateTimeList] = Field(None, description="An unweighted list of averaging observation date and times.")
  """
  An unweighted list of averaging observation date and times.
  """
  averagingObservations: Optional[AveragingObservationList] = Field(None, description="A weighted list of averaging observation date and times.")
  """
  A weighted list of averaging observation date and times.
  """
  marketDisruption: Optional[AttributeWithMeta[MarketDisruptionEnum] | MarketDisruptionEnum] = Field(None, description="The market disruption event as defined by ISDA 2002 Definitions.")
  """
  The market disruption event as defined by ISDA 2002 Definitions.
  """
  schedule: List[AveragingSchedule] = Field([], description="A schedule for generating averaging observation dates.")
  """
  A schedule for generating averaging observation dates.
  """
  
  @rosetta_condition
  def condition_0_AveragingPeriodChoice(self):
    """
     Choice rule to represent an FpML choice construct between unweighted and weighted averaging date and times.
    """
    return self.check_one_of_constraint('averagingDateTimes', 'averagingObservations', necessity=False)

from cdm.base.datetime.DateTimeList import DateTimeList
from cdm.product.common.schedule.AveragingObservationList import AveragingObservationList
from cdm.observable.event.MarketDisruptionEnum import MarketDisruptionEnum
from cdm.base.datetime.AveragingSchedule import AveragingSchedule

AveragingPeriod.update_forward_refs()
