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

__all__ = ['AveragingObservationList']


class AveragingObservationList(BaseDataClass):
  """
  An unordered list of weighted averaging observations.
  """
  averagingObservation: List[WeightedAveragingObservation] = Field([], description="A single weighted averaging observation.")
  """
  A single weighted averaging observation.
  """
  @rosetta_condition
  def cardinality_averagingObservation(self):
    return check_cardinality(self.averagingObservation, 1, None)
  

from cdm.product.common.schedule.WeightedAveragingObservation import WeightedAveragingObservation

AveragingObservationList.update_forward_refs()
