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

__all__ = ['Barrier']


class Barrier(BaseDataClass):
  """
  As per ISDA 2002 Definitions.
  """
  barrierCap: Optional[TriggerEvent] = Field(None, description="A trigger level approached from beneath.")
  """
  A trigger level approached from beneath.
  """
  barrierFloor: Optional[TriggerEvent] = Field(None, description="A trigger level approached from above.")
  """
  A trigger level approached from above.
  """

from cdm.observable.event.TriggerEvent import TriggerEvent

Barrier.update_forward_refs()
