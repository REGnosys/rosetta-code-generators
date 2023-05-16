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

__all__ = ['EventInstruction']


class EventInstruction(BaseDataClass):
  """
  Specifies instructions to create a BusinessEvent.
  """
  effectiveDate: Optional[date] = Field(None, description="The date on which the event contractually takes effect, when different from the event date.")
  """
  The date on which the event contractually takes effect, when different from the event date.
  """
  eventDate: Optional[date] = Field(None, description="The date of the business event.")
  """
  The date of the business event.
  """
  instruction: List[Instruction] = Field([], description="The instructions for creation of a business event.")
  """
  The instructions for creation of a business event.
  """
  intent: Optional[EventIntentEnum] = Field(None, description="The event intent.")
  """
  The event intent.
  """

from cdm.event.common.Instruction import Instruction
from cdm.event.common.EventIntentEnum import EventIntentEnum

EventInstruction.update_forward_refs()
