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

__all__ = ['FallbackRateParameters']


class FallbackRateParameters(BaseDataClass):
  """
  Defines the structure needed to represent fallback rate parameters. This type is used to represent modular computed rates in interestRatePayouts.
  """
  calculationParameters: Optional[FloatingRateCalculationParameters] = Field(None, description="Support for modular calculated rates, such such as lockout compound calculations.")
  """
  Support for modular calculated rates, such such as lockout compound calculations.
  """
  effectiveDate: Optional[date] = Field(None, description="The date the fallback rate takes effect.")
  """
  The date the fallback rate takes effect.
  """
  floatingRateIndex: FloatingRateIndexEnum = Field(..., description="The floating rate index that is used as the basis of the fallback rate.")
  """
  The floating rate index that is used as the basis of the fallback rate.
  """
  spreadAdjustment: Optional[Decimal] = Field(None, description="The economic spread applied to the underlying fallback rate to replicate the original risky rate.")
  """
  The economic spread applied to the underlying fallback rate to replicate the original risky rate.
  """

from cdm.observable.asset.calculatedrate.FloatingRateCalculationParameters import FloatingRateCalculationParameters
from cdm.base.staticdata.asset.rates.FloatingRateIndexEnum import FloatingRateIndexEnum

FallbackRateParameters.update_forward_refs()
