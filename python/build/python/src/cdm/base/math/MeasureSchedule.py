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

__all__ = ['MeasureSchedule']

from cdm.base.math.MeasureBase import MeasureBase

class MeasureSchedule(MeasureBase):
  """
  A set of measures, all in the same unit, where the values are defined through a schedule of steps. The initial value may be defined either as part of the steps, or using the single amount attribute.
  """
  datedValue: List[DatedValue] = Field([], description="A schedule of step date and value pairs. On each step date the associated step value becomes effective. The step dates are used to order the steps by ascending order. This attribute is optional so the data type may be used to define a schedule with a single value.")
  """
  A schedule of step date and value pairs. On each step date the associated step value becomes effective. The step dates are used to order the steps by ascending order. This attribute is optional so the data type may be used to define a schedule with a single value.
  """
  
  @rosetta_condition
  def condition_0_ValueExists(self):
    """
    A schedule may be specified as a single value or as a set of date-value pairs. Both attributes may be specified, in which case the single amount number is the initial value.
    """
    return (((self.value) is not None) or ((self.datedValue) is not None))

from cdm.base.math.DatedValue import DatedValue

MeasureSchedule.update_forward_refs()
