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

__all__ = ['DateRelativeToValuationDates']


class DateRelativeToValuationDates(BaseDataClass):
  """
  A data to:  provide the ability to point to multiple payment nodes in the document through the unbounded paymentDatesReference.
  """
  valuationDatesReference: List[AttributeWithReference | PerformanceValuationDates] = Field([], description="A set of href pointers to valuation period dates defined somewhere else in the document.")
  """
  A set of href pointers to valuation period dates defined somewhere else in the document.
  """
  @rosetta_condition
  def cardinality_valuationDatesReference(self):
    return check_cardinality(self.valuationDatesReference, 1, None)
  

from cdm.observable.asset.PerformanceValuationDates import PerformanceValuationDates

DateRelativeToValuationDates.update_forward_refs()
