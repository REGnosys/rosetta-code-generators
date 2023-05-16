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

__all__ = ['ObservationTerms']


class ObservationTerms(BaseDataClass):
  """
  Class containing terms that are associated with observing a price/benchmark/index across either single or multiple observations. 
  """
  calculationPeriodDates: Optional[CalculationPeriodDates] = Field(None, description="Defines parameters used to generate the calculation period dates schedule, including the specification of any initial or final stub calculation periods. A calculation period schedule consists of an optional initial stub calculation period, one or more regular calculation periods and an optional final stub calculation period. In the absence of any initial or final stub calculation periods, the regular part of the calculation period schedule is assumed to be between the effective date and the termination date. No implicit stubs are allowed, i.e. stubs must be explicitly specified using an appropriate combination of firstPeriodStartDate, firstRegularPeriodStartDate and lastRegularPeriodEndDate.")
  """
  Defines parameters used to generate the calculation period dates schedule, including the specification of any initial or final stub calculation periods. A calculation period schedule consists of an optional initial stub calculation period, one or more regular calculation periods and an optional final stub calculation period. In the absence of any initial or final stub calculation periods, the regular part of the calculation period schedule is assumed to be between the effective date and the termination date. No implicit stubs are allowed, i.e. stubs must be explicitly specified using an appropriate combination of firstPeriodStartDate, firstRegularPeriodStartDate and lastRegularPeriodEndDate.
  """
  informationSource: Optional[FxSpotRateSource] = Field(None, description="The information source where a published or displayed market rate will be obtained, e.g. Telerate Page 3750.")
  """
  The information source where a published or displayed market rate will be obtained, e.g. Telerate Page 3750.
  """
  numberOfObservationDates: Optional[int] = Field(None, description="The number of observation dates between observation start date and observation end date.")
  """
  The number of observation dates between observation start date and observation end date.
  """
  observable: Optional[Observable] = Field(None, description="Specifies the object to be observed for a price, it could be an asset or a reference.")
  """
  Specifies the object to be observed for a price, it could be an asset or a reference.
  """
  observationDates: ObservationDates = Field(..., description="Describes date details for a set of observation dates in parametric or non-parametric form.")
  """
  Describes date details for a set of observation dates in parametric or non-parametric form.
  """
  precision: Optional[Rounding] = Field(None, description="Defines rounding rules and precision to be used in the rounding of observations.")
  """
  Defines rounding rules and precision to be used in the rounding of observations.
  """
  pricingTime: Optional[BusinessCenterTime] = Field(None, description="Defines time in respect to a business calendar location that the price/benchmark/index is observed")
  """
  Defines time in respect to a business calendar location that the price/benchmark/index is observed
  """
  pricingTimeType: Optional[TimeTypeEnum] = Field(None, description="The enumerated values to specify points in the day when option exercise and valuation can occur.")
  """
  The enumerated values to specify points in the day when option exercise and valuation can occur.
  """
  
  @rosetta_condition
  def condition_0_PricingTime(self):
    """
    Checks that a pricing time is specified either explicitly (through the pricing time) or implicitly (through a pricing time type different to Specific Time). If Specific Time is defined as pricing time type (i.e. no implicit time value), the condition checks that an explicit pricing time is provided.
    """
    def _then_fn0():
      return ((self.pricingTime) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.pricingTimeType, "=", TimeTypeEnum.SPECIFIC_TIME), _then_fn0, _else_fn0)

from cdm.product.common.schedule.CalculationPeriodDates import CalculationPeriodDates
from cdm.observable.asset.FxSpotRateSource import FxSpotRateSource
from cdm.observable.asset.Observable import Observable
from cdm.product.common.schedule.ObservationDates import ObservationDates
from cdm.base.math.Rounding import Rounding
from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime
from cdm.observable.common.TimeTypeEnum import TimeTypeEnum

ObservationTerms.update_forward_refs()
