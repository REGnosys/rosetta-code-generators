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

__all__ = ['TriggerEvent']


class TriggerEvent(BaseDataClass):
  """
  Observation point for trigger.
  """
  featurePayment: Optional[FeaturePayment] = Field(None, description="The feature payment, i.e. the payment made following trigger occurrence.")
  """
  The feature payment, i.e. the payment made following trigger occurrence.
  """
  schedule: List[AveragingSchedule] = Field([], description="A derivative schedule.")
  """
  A derivative schedule.
  """
  trigger: Trigger = Field(..., description="The trigger level")
  """
  The trigger level
  """
  triggerDates: Optional[DateList] = Field(None, description="The trigger Dates.")
  """
  The trigger Dates.
  """

from cdm.observable.event.FeaturePayment import FeaturePayment
from cdm.base.datetime.AveragingSchedule import AveragingSchedule
from cdm.observable.event.Trigger import Trigger
from cdm.base.datetime.DateList import DateList

TriggerEvent.update_forward_refs()
