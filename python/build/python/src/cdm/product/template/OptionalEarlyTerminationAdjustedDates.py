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

__all__ = ['OptionalEarlyTerminationAdjustedDates']


class OptionalEarlyTerminationAdjustedDates(BaseDataClass):
  """
  A data defining:  the adjusted dates associated with an optional early termination provision.
  """
  earlyTerminationEvent: List[EarlyTerminationEvent] = Field([], description="The adjusted dates associated with an individual early termination date.")
  """
  The adjusted dates associated with an individual early termination date.
  """
  @rosetta_condition
  def cardinality_earlyTerminationEvent(self):
    return check_cardinality(self.earlyTerminationEvent, 1, None)
  

from cdm.product.template.EarlyTerminationEvent import EarlyTerminationEvent

OptionalEarlyTerminationAdjustedDates.update_forward_refs()
