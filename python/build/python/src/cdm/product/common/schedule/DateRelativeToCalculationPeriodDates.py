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

__all__ = ['DateRelativeToCalculationPeriodDates']


class DateRelativeToCalculationPeriodDates(BaseDataClass):
  """
  A data to:  provide the ability to point to multiple payment nodes in the document through the unbounded paymentDatesReference.
  """
  calculationPeriodDatesReference: List[AttributeWithReference | CalculationPeriodDates] = Field([], description="A set of href pointers to calculation period dates defined somewhere else in the document.")
  """
  A set of href pointers to calculation period dates defined somewhere else in the document.
  """
  @rosetta_condition
  def cardinality_calculationPeriodDatesReference(self):
    return check_cardinality(self.calculationPeriodDatesReference, 1, None)
  

from cdm.product.common.schedule.CalculationPeriodDates import CalculationPeriodDates

DateRelativeToCalculationPeriodDates.update_forward_refs()
