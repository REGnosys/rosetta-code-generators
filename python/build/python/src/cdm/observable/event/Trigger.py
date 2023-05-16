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

__all__ = ['Trigger']


class Trigger(BaseDataClass):
  """
  Trigger point at which feature is effective.
  """
  creditEvents: Optional[CreditEvents] = Field(None, description="")
  creditEventsReference: Optional[AttributeWithReference | CreditEvents] = Field(None, description="")
  level: Optional[Decimal] = Field(None, description="The trigger level.")
  """
  The trigger level.
  """
  levelPercentage: Optional[Decimal] = Field(None, description="The trigger level percentage.")
  """
  The trigger level percentage.
  """
  triggerTimeType: Optional[TriggerTimeTypeEnum] = Field(None, description="The valuation time type of knock condition.")
  """
  The valuation time type of knock condition.
  """
  triggerType: Optional[TriggerTypeEnum] = Field(None, description="The Triggering condition.")
  """
  The Triggering condition.
  """
  
  @rosetta_condition
  def condition_0_Choice1(self):
    """
     Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('level', 'levelPercentage', 'creditEvents', 'creditEventsReference', necessity=True)

from cdm.observable.event.CreditEvents import CreditEvents
from cdm.observable.event.TriggerTimeTypeEnum import TriggerTimeTypeEnum
from cdm.observable.event.TriggerTypeEnum import TriggerTypeEnum

Trigger.update_forward_refs()
