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

__all__ = ['CalculationPeriodBase']


class CalculationPeriodBase(BaseDataClass):
  """
  The calculation period adjusted start and end dates, which are the baseline arguments needed to compute an interest accrual calculation.
  """
  adjustedEndDate: Optional[date] = Field(None, description="The calculation period end date, adjusted according to any relevant business day convention.")
  """
  The calculation period end date, adjusted according to any relevant business day convention.
  """
  adjustedStartDate: Optional[date] = Field(None, description="The calculation period start date, adjusted according to any relevant business day convention.")
  """
  The calculation period start date, adjusted according to any relevant business day convention.
  """


CalculationPeriodBase.update_forward_refs()
