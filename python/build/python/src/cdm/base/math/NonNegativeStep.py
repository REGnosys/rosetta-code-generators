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

__all__ = ['NonNegativeStep']


class NonNegativeStep(BaseDataClass):
  """
  A class defining a step date and non-negative step value pair. This step definitions are used to define varying rate or amount schedules, e.g. a notional amortisation or a step-up coupon schedule.
  """
  stepDate: date = Field(..., description="The date on which the associated stepValue becomes effective. This day may be subject to adjustment in accordance with a business day convention.")
  """
  The date on which the associated stepValue becomes effective. This day may be subject to adjustment in accordance with a business day convention.
  """
  stepValue: Decimal = Field(..., description="The non-negative rate or amount which becomes effective on the associated stepDate. A rate of 5% would be represented as 0.05.")
  """
  The non-negative rate or amount which becomes effective on the associated stepDate. A rate of 5% would be represented as 0.05.
  """
  
  @rosetta_condition
  def condition_0_StepValue(self):
    """
    FpML specified stepValue as a NonNegativeDecimal.
    """
    return all_elements(self.stepValue, ">=", 0.0)


NonNegativeStep.update_forward_refs()
