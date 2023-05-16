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

__all__ = ['CancelableProvisionAdjustedDates']


class CancelableProvisionAdjustedDates(BaseDataClass):
  """
  A data to:  define the adjusted dates for a cancelable provision on a swap transaction.
  """
  cancellationEvent: List[CancellationEvent] = Field([], description="The adjusted dates for an individual cancellation date.")
  """
  The adjusted dates for an individual cancellation date.
  """
  @rosetta_condition
  def cardinality_cancellationEvent(self):
    return check_cardinality(self.cancellationEvent, 1, None)
  

from cdm.product.template.CancellationEvent import CancellationEvent

CancelableProvisionAdjustedDates.update_forward_refs()
