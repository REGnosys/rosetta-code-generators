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

__all__ = ['FloatingRateCalculationParameters']


class FloatingRateCalculationParameters(BaseDataClass):
  """
  Defines the structures needed to represent the calculation parameters for daily averaged and compounded modular rates as defined in the 2021 ISDA Definitions in Section 7. This type is used to represent modular computed rates in interestRatePayouts.
  """
  applicableBusinessDays: Optional[BusinessCenters] = Field(None, description="the business days that are applicable for the calculation.")
  """
  the business days that are applicable for the calculation.
  """
  calculationMethod: CalculationMethodEnum = Field(..., description="calculation type (averaging or compounding).")
  """
  calculation type (averaging or compounding).
  """
  lockoutCalculation: Optional[OffsetCalculation] = Field(None, description="any lockout  parameters if applicable.")
  """
  any lockout  parameters if applicable.
  """
  lookbackCalculation: Optional[OffsetCalculation] = Field(None, description="any lookback  parameters if applicable.")
  """
  any lookback  parameters if applicable.
  """
  observationParameters: Optional[ObservationParameters] = Field(None, description=" any applicable observation parameters, such as daily caps or floors.")
  """
   any applicable observation parameters, such as daily caps or floors.
  """
  observationShiftCalculation: Optional[ObservationShiftCalculation] = Field(None, description="any obervation shift parameters if applicable.")
  """
  any obervation shift parameters if applicable.
  """

from cdm.base.datetime.BusinessCenters import BusinessCenters
from cdm.observable.asset.calculatedrate.CalculationMethodEnum import CalculationMethodEnum
from cdm.observable.asset.calculatedrate.OffsetCalculation import OffsetCalculation
from cdm.observable.asset.calculatedrate.ObservationParameters import ObservationParameters
from cdm.observable.asset.calculatedrate.ObservationShiftCalculation import ObservationShiftCalculation

FloatingRateCalculationParameters.update_forward_refs()
