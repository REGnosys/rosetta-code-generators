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

__all__ = ['ExtensionEvent']


class ExtensionEvent(BaseDataClass):
  """
  A data to:  define the adjusted dates associated with an individual extension event.
  """
  adjustedExerciseDate: date = Field(..., description="The date on which option exercise takes place. This date should already be adjusted for any applicable business day convention.")
  """
  The date on which option exercise takes place. This date should already be adjusted for any applicable business day convention.
  """
  adjustedExtendedTerminationDate: date = Field(..., description="The termination date if an extendible provision is exercised. This date should already be adjusted for any applicable business day convention.")
  """
  The termination date if an extendible provision is exercised. This date should already be adjusted for any applicable business day convention.
  """
  
  @rosetta_condition
  def condition_0_FpML_ird_42(self):
    """
    FpML validation rule ird-42 - adjustedExerciseDate must be before adjustedExtendedTerminationDate.
    """
    return all_elements(self.adjustedExerciseDate, "<", self.adjustedExtendedTerminationDate)


ExtensionEvent.update_forward_refs()
