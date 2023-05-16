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

__all__ = ['ExercisePeriod']


class ExercisePeriod(BaseDataClass):
  """
  This defines the time interval to the start of the exercise period, i.e. the earliest exercise date, and the frequency of subsequent exercise dates (if any).
  """
  earliestExerciseDateTenor: Period = Field(..., description="The time interval to the first (and possibly only) exercise date in the exercise period.")
  """
  The time interval to the first (and possibly only) exercise date in the exercise period.
  """
  exerciseFrequency: Optional[Period] = Field(None, description="The frequency of subsequent exercise dates in the exercise period following the earliest exercise date. An interval of 1 day should be used to indicate an American style exercise period.")
  """
  The frequency of subsequent exercise dates in the exercise period following the earliest exercise date. An interval of 1 day should be used to indicate an American style exercise period.
  """

from cdm.base.datetime.Period import Period

ExercisePeriod.update_forward_refs()
