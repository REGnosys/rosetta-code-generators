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

__all__ = ['FloatingRateSettingDetails']


class FloatingRateSettingDetails(BaseDataClass):
  """
  Type for reporting the raw (untreated) observed or calculated rate for a calculation period.  If this is a calculated rate, it allows details of the observations and the resulting rate to be returned.
  """
  calculationDetails: Optional[CalculatedRateDetails] = Field(None, description="Calculated rate details (observation dates, values, and weights).")
  """
  Calculated rate details (observation dates, values, and weights).
  """
  floatingRate: Decimal = Field(..., description="The resulting rate that was observed or calculated.")
  """
  The resulting rate that was observed or calculated.
  """
  observationDate: Optional[date] = Field(None, description="The day upon which the rate was observed (for term rates).")
  """
  The day upon which the rate was observed (for term rates).
  """
  resetDate: Optional[date] = Field(None, description="The day for which the rate is needed (e.g. period beginning or end date).")
  """
  The day for which the rate is needed (e.g. period beginning or end date).
  """

from cdm.observable.asset.calculatedrate.CalculatedRateDetails import CalculatedRateDetails

FloatingRateSettingDetails.update_forward_refs()
