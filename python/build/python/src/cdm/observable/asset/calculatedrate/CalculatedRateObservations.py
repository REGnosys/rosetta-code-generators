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

__all__ = ['CalculatedRateObservations']


class CalculatedRateObservations(BaseDataClass):
  """
  Type for reporting observations that went into the final reported rate.
  """
  observationDates: List[date] = Field([], description="The observation date upon which the rate is observed.")
  """
  The observation date upon which the rate is observed.
  """
  observedRates: List[Decimal] = Field([], description="The value observed for that date")
  """
  The value observed for that date
  """
  processedRates: List[Decimal] = Field([], description="The value after any processing, such as application of caps or floors.")
  """
  The value after any processing, such as application of caps or floors.
  """
  weights: List[Decimal] = Field([], description="The corresponding weight for each date.")
  """
  The corresponding weight for each date.
  """


CalculatedRateObservations.update_forward_refs()
