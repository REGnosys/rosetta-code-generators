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

__all__ = ['CalculationPeriodDates']


class CalculationPeriodDates(BaseDataClass):
  """
  A data for:  defining the parameters used to generate the calculation period dates schedule, including the specification of any initial or final stub calculation periods. A calculation period schedule consists of an optional initial stub calculation period, one or more regular calculation periods and an optional final stub calculation period. In the absence of any initial or final stub calculation periods, the regular part of the calculation period schedule is assumed to be between the effective date and the termination date. No implicit stubs are allowed, i.e. stubs must be explicitly specified using an appropriate combination of firstPeriodStartDate, firstRegularPeriodStartDate and lastRegularPeriodEndDate.
  """
  calculationPeriodDatesAdjustments: Optional[BusinessDayAdjustments] = Field(None, description="The specification of the business day convention and financial business centers used for adjusting any calculation period date if it would otherwise fall on a day that is not a business day in the specified business center.")
  """
  The specification of the business day convention and financial business centers used for adjusting any calculation period date if it would otherwise fall on a day that is not a business day in the specified business center.
  """
  calculationPeriodFrequency: Optional[CalculationPeriodFrequency] = Field(None, description="The frequency at which calculation period end dates occur with the regular part of the calculation period schedule and their roll date convention.")
  """
  The frequency at which calculation period end dates occur with the regular part of the calculation period schedule and their roll date convention.
  """
  effectiveDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The first day of the terms of the trade. This day may be subject to adjustment in accordance with a business day convention.")
  """
  The first day of the terms of the trade. This day may be subject to adjustment in accordance with a business day convention.
  """
  firstCompoundingPeriodEndDate: Optional[date] = Field(None, description="The end date of the initial compounding period when compounding is applicable. It must only be specified when the compoundingMethod element is present and not equal to a value of None. This date may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments.")
  """
  The end date of the initial compounding period when compounding is applicable. It must only be specified when the compoundingMethod element is present and not equal to a value of None. This date may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments.
  """
  firstPeriodStartDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The start date of the calculation period. FpML specifies that for interest rate swaps this date must only be specified if it is not equal to the effective date. It is always specified in the case of equity swaps and credit default swaps with periodic payments. This date may be subject to adjustment in accordance with a business day convention.")
  """
  The start date of the calculation period. FpML specifies that for interest rate swaps this date must only be specified if it is not equal to the effective date. It is always specified in the case of equity swaps and credit default swaps with periodic payments. This date may be subject to adjustment in accordance with a business day convention.
  """
  firstRegularPeriodStartDate: Optional[date] = Field(None, description="The start date of the regular part of the calculation period schedule. It must only be specified if there is an initial stub calculation period. This day may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments.")
  """
  The start date of the regular part of the calculation period schedule. It must only be specified if there is an initial stub calculation period. This day may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments.
  """
  lastRegularPeriodEndDate: Optional[date] = Field(None, description="The end date of the regular part of the calculation period schedule. It must only be specified if there is a final stub calculation period. This day may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments.")
  """
  The end date of the regular part of the calculation period schedule. It must only be specified if there is a final stub calculation period. This day may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments.
  """
  stubPeriodType: Optional[StubPeriodTypeEnum] = Field(None, description="Method to allocate any irregular period remaining after regular periods have been allocated between the effective and termination date.")
  """
  Method to allocate any irregular period remaining after regular periods have been allocated between the effective and termination date.
  """
  terminationDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The last day of the terms of the trade. This date may be subject to adjustments in accordance with the business day convention. It can also be specified in relation to another scheduled date (e.g. the last payment date).")
  """
  The last day of the terms of the trade. This date may be subject to adjustments in accordance with the business day convention. It can also be specified in relation to another scheduled date (e.g. the last payment date).
  """
  
  @rosetta_condition
  def condition_0_FpML_ird_16(self):
    """
    FpML validation rule ird-16 - If firstRegularPeriodStartDate exists within any element of type CalculationPeriodDates, then terminationDate/unadjustedDate must be after firstRegularPeriodStartDate. This data rule applies within a given interest rate payout component.
    """
    def _then_fn0():
      return all_elements(self.terminationDate.adjustableDate.unadjustedDate, ">", self.firstRegularPeriodStartDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.firstRegularPeriodStartDate) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_FpML_ird_17(self):
    """
    FpML validation rule ird-17 - If lastRegularPeriodEndDate exists, then terminationDate/unadjustedDate must be after lastRegularPeriodEndDate. This data rule applies within a given interest rate payout component.
    """
    def _then_fn0():
      return all_elements(self.terminationDate.adjustableDate.unadjustedDate, ">", self.lastRegularPeriodEndDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.lastRegularPeriodEndDate) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_FpML_ird_18(self):
    """
    FpML validation rule ird-18 - If firstRegularPeriodStartDate exists, and if lastRegularPeriodEndDate exists, then lastRegularPeriodEndDate must be after firstRegularPeriodStartDate. This data rule applies within a given interest rate payout component.
    """
    def _then_fn0():
      return all_elements(self.lastRegularPeriodEndDate, ">", self.firstRegularPeriodStartDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.firstRegularPeriodStartDate) is not None) and ((self.lastRegularPeriodEndDate) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_FpML_ird_20(self):
    """
    FpML validation rule ird-20 - If lastRegularPeriodEndDate exists, then lastRegularPeriodEndDate must be after effectiveDate/unadjustedDate. This data rule applies within a given interest rate payout component.
    """
    def _then_fn0():
      return all_elements(self.lastRegularPeriodEndDate, ">", self.effectiveDate.adjustableDate.unadjustedDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.lastRegularPeriodEndDate) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_FpML_ird_21(self):
    """
    FpML validation rule ird-21 - If firstPeriodStartDate exists, then firstPeriodStartDate/unadjustedDate must be before effectiveDate/unadjustedDate. This data rule applies within a given interest rate payout component.
    """
    def _then_fn0():
      return all_elements(self.firstPeriodStartDate.adjustableDate.unadjustedDate, "<", self.effectiveDate.adjustableDate.unadjustedDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.firstPeriodStartDate) is not None) and ((self.effectiveDate) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_5_FpML_ird_22(self):
    """
    FpML validation rule ird-22 - If firstPeriodStartDate exists, and if firstRegularPeriodStartDate exists, then firstPeriodStartDate/unadjustedDate must be before firstRegularPeriodStartDate. This data rule applies within a given interest rate payout component.
    """
    def _then_fn0():
      return all_elements(self.firstPeriodStartDate.adjustableDate.unadjustedDate, "<", self.firstRegularPeriodStartDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.firstPeriodStartDate) is not None) and ((self.firstRegularPeriodStartDate) is not None)), _then_fn0, _else_fn0)

from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments
from cdm.base.datetime.CalculationPeriodFrequency import CalculationPeriodFrequency
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.product.common.schedule.StubPeriodTypeEnum import StubPeriodTypeEnum

CalculationPeriodDates.update_forward_refs()
