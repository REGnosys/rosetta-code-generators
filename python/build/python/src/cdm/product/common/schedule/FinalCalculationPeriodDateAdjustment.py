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

__all__ = ['FinalCalculationPeriodDateAdjustment']


class FinalCalculationPeriodDateAdjustment(BaseDataClass):
  """
  A data to:  define business date convention adjustment to final payment period per leg.
  """
  businessDayConvention: BusinessDayConventionEnum = Field(..., description="Override business date convention. This takes precedence over leg level information.")
  """
  Override business date convention. This takes precedence over leg level information.
  """
  relevantUnderlyingDateReference: AttributeWithReference | AdjustableOrRelativeDates = Field(..., description="Reference to the unadjusted cancellation effective dates.")
  """
  Reference to the unadjusted cancellation effective dates.
  """
  swapStreamReference: AttributeWithReference | InterestRatePayout = Field(..., description="Reference to the leg, where date adjustments may apply.")
  """
  Reference to the leg, where date adjustments may apply.
  """

from cdm.base.datetime.BusinessDayConventionEnum import BusinessDayConventionEnum
from cdm.base.datetime.AdjustableOrRelativeDates import AdjustableOrRelativeDates
from cdm.product.asset.InterestRatePayout import InterestRatePayout

FinalCalculationPeriodDateAdjustment.update_forward_refs()
