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

__all__ = ['ObservationSchedule']


class ObservationSchedule(BaseDataClass):
  """
  Specifies a single date on which market observations take place and specifies optional associated weighting.
  """
  date: Optional[AdjustableOrAdjustedDate] = Field(None, description="Specifies an adjusted or unadjusted date for a market observation.")
  """
  Specifies an adjusted or unadjusted date for a market observation.
  """
  observationReference: Optional[str] = Field(None, description="Specifies an identification key for the market observation. This attribute can be used as a reference to assign weights to a series of dates defined in a parametricSchedule.")
  """
  Specifies an identification key for the market observation. This attribute can be used as a reference to assign weights to a series of dates defined in a parametricSchedule.
  """
  weight: Optional[Decimal] = Field(None, description="Specifies the degree of importance of the observation.")
  """
  Specifies the degree of importance of the observation.
  """

from cdm.base.datetime.AdjustableOrAdjustedDate import AdjustableOrAdjustedDate

ObservationSchedule.update_forward_refs()
