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

__all__ = ['CalculatedRateObservationDatesAndWeights']


class CalculatedRateObservationDatesAndWeights(BaseDataClass):
  """
  Type for reporting the observations dates and the corresponding weights going into a daily calculated rate
  """
  observationDates: List[date] = Field([], description="The observation date upon which the rate is observed.")
  """
  The observation date upon which the rate is observed.
  """
  weights: List[Decimal] = Field([], description="The corresponding weight for each date.")
  """
  The corresponding weight for each date.
  """


CalculatedRateObservationDatesAndWeights.update_forward_refs()
