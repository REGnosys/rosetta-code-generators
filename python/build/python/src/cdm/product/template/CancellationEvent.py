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

__all__ = ['CancellationEvent']


class CancellationEvent(BaseDataClass):
  """
  The adjusted dates for a specific cancellation date, including the adjusted exercise date and adjusted termination date.
  """
  adjustedEarlyTerminationDate: date = Field(..., description="The early termination date that is applicable if an early termination provision is exercised. This date should already be adjusted for any applicable business day convention.")
  """
  The early termination date that is applicable if an early termination provision is exercised. This date should already be adjusted for any applicable business day convention.
  """
  adjustedExerciseDate: date = Field(..., description="The date on which option exercise takes place. This date should already be adjusted for any applicable business day convention.")
  """
  The date on which option exercise takes place. This date should already be adjusted for any applicable business day convention.
  """


CancellationEvent.update_forward_refs()
