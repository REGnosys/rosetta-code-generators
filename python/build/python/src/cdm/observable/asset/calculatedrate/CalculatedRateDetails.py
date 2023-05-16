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

__all__ = ['CalculatedRateDetails']


class CalculatedRateDetails(BaseDataClass):
  """
  Type for reporting details of calculated rates, including the observations that went into the final reported rate.
  """
  aggregateValue: Optional[Decimal] = Field(None, description="The total sum or product of all the individual terms that went into the calculated rate.")
  """
  The total sum or product of all the individual terms that went into the calculated rate.
  """
  aggregateWeight: Optional[Decimal] = Field(None, description="The total weight of all the terms that went into the calculated rate.")
  """
  The total weight of all the terms that went into the calculated rate.
  """
  calculatedRate: Optional[Decimal] = Field(None, description="The resulting calculated weight.")
  """
  The resulting calculated weight.
  """
  compoundedGrowth: List[Decimal] = Field([], description="The compounding curve, showing how the initial value grew during the calculation period.")
  """
  The compounding curve, showing how the initial value grew during the calculation period.
  """
  growthFactor: List[Decimal] = Field([], description="The daily growth factors, showing the weighted rates divided by the day count basis plus one, giving how much the value grows for each step in the calculation.")
  """
  The daily growth factors, showing the weighted rates divided by the day count basis plus one, giving how much the value grows for each step in the calculation.
  """
  observations: Optional[CalculatedRateObservations] = Field(None, description="The observation dates and weights for each observation date.")
  """
  The observation dates and weights for each observation date.
  """
  weightedRates: List[Decimal] = Field([], description="The weighted value of each observation.")
  """
  The weighted value of each observation.
  """

from cdm.observable.asset.calculatedrate.CalculatedRateObservations import CalculatedRateObservations

CalculatedRateDetails.update_forward_refs()
