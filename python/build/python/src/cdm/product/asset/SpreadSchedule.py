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

__all__ = ['SpreadSchedule']

from cdm.product.common.schedule.RateSchedule import RateSchedule

class SpreadSchedule(RateSchedule):
  """
  Adds an optional spread type element to the Schedule to identify a long or short spread value.
  """
  spreadScheduleType: Optional[AttributeWithMeta[SpreadScheduleTypeEnum] | SpreadScheduleTypeEnum] = Field(None, description="An element which purpose is to identify a long or short spread value.")
  """
  An element which purpose is to identify a long or short spread value.
  """

from cdm.product.asset.SpreadScheduleTypeEnum import SpreadScheduleTypeEnum

SpreadSchedule.update_forward_refs()
