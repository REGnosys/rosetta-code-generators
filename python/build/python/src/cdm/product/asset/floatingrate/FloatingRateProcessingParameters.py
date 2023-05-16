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

__all__ = ['FloatingRateProcessingParameters']


class FloatingRateProcessingParameters(BaseDataClass):
  """
  Type to hold the processing parameters that should be or were used to calculate a floating amount.  These parameters can vary over a schedule so this type holds the acutal values applicable to this calculation.
  """
  capRate: Optional[Decimal] = Field(None, description="capt to be applied to the floating rate.")
  """
  capt to be applied to the floating rate.
  """
  floorRate: Optional[Decimal] = Field(None, description="floor to be applied to the floating rate.")
  """
  floor to be applied to the floating rate.
  """
  initialRate: Optional[Price] = Field(None, description="The rate to be applied for the initial period.")
  """
  The rate to be applied for the initial period.
  """
  multiplier: Optional[Decimal] = Field(None, description="floating rate multiplier.")
  """
  floating rate multiplier.
  """
  negativeTreatment: Optional[NegativeInterestRateTreatmentEnum] = Field(None, description="How to handle negative interest rates.")
  """
  How to handle negative interest rates.
  """
  rounding: Optional[Rounding] = Field(None, description="THe final rate rounding to be applied.")
  """
  THe final rate rounding to be applied.
  """
  spread: Optional[Decimal] = Field(None, description="spread to be added to the floating rate.")
  """
  spread to be added to the floating rate.
  """
  treatment: Optional[RateTreatmentEnum] = Field(None, description="US rate treatment (Bond Equivalent Yield or Money Market Yield, if applicable.")
  """
  US rate treatment (Bond Equivalent Yield or Money Market Yield, if applicable.
  """

from cdm.observable.asset.Price import Price
from cdm.product.asset.NegativeInterestRateTreatmentEnum import NegativeInterestRateTreatmentEnum
from cdm.base.math.Rounding import Rounding
from cdm.product.asset.RateTreatmentEnum import RateTreatmentEnum

FloatingRateProcessingParameters.update_forward_refs()
