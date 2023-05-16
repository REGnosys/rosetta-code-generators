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

__all__ = ['ExerciseEvent']


class ExerciseEvent(BaseDataClass):
  """
  A data defining:  the adjusted dates associated with a particular exercise event.
  """
  adjustedCashSettlementPaymentDate: Optional[date] = Field(None, description="The date on which the cash settlement amount is paid. This date should already be adjusted for any applicable business day convention.")
  """
  The date on which the cash settlement amount is paid. This date should already be adjusted for any applicable business day convention.
  """
  adjustedCashSettlementValuationDate: Optional[date] = Field(None, description="The date by which the cash settlement amount must be agreed. This date should already be adjusted for any applicable business day convention.")
  """
  The date by which the cash settlement amount must be agreed. This date should already be adjusted for any applicable business day convention.
  """
  adjustedExerciseDate: date = Field(..., description="The date on which the option exercise takes place. This date should already be adjusted for any applicable business day convention.")
  """
  The date on which the option exercise takes place. This date should already be adjusted for any applicable business day convention.
  """
  adjustedExerciseFeePaymentDate: Optional[date] = Field(None, description="The date on which the exercise fee amount is paid. This date should already be adjusted for any applicable business day convention.")
  """
  The date on which the exercise fee amount is paid. This date should already be adjusted for any applicable business day convention.
  """
  adjustedRelevantSwapEffectiveDate: date = Field(..., description="The effective date of the underlying swap associated with a given exercise date. This date should already be adjusted for any applicable business day convention.")
  """
  The effective date of the underlying swap associated with a given exercise date. This date should already be adjusted for any applicable business day convention.
  """


ExerciseEvent.update_forward_refs()
