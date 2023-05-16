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

__all__ = ['ResetDates']


class ResetDates(BaseDataClass):
  """
  A data defining:  the parameters used to generate the reset dates schedule and associated fixing dates. The reset dates are the dates on which the new index value (which is observed on the fixing date) is applied for each period and on which the interest rate hence begins to accrue.
  """
  calculationPeriodDatesReference: Optional[AttributeWithReference | CalculationPeriodDates] = Field(None, description="A pointer style reference to the associated calculation period dates component defined elsewhere in the document.")
  """
  A pointer style reference to the associated calculation period dates component defined elsewhere in the document.
  """
  finalFixingDate: Optional[AdjustableDate] = Field(None, description="This attribute is not part of the FpML ResetDate, and has been added as part of the CDM to support the credit derivatives final fixing date.")
  """
  This attribute is not part of the FpML ResetDate, and has been added as part of the CDM to support the credit derivatives final fixing date.
  """
  fixingDates: Optional[RelativeDateOffset] = Field(None, description="The fixing dates are the dates on which the index values are observed. The fixing dates are specified by reference to the reset date through business days offset and an associated set of financial business centers. Normally these offset calculation rules will be those specified in the ISDA definition for the relevant floating rate index (ISDA's Floating Rate Option). However, non-standard offset calculation rules may apply for a trade if mutually agreed by the principal parties to the transaction.")
  """
  The fixing dates are the dates on which the index values are observed. The fixing dates are specified by reference to the reset date through business days offset and an associated set of financial business centers. Normally these offset calculation rules will be those specified in the ISDA definition for the relevant floating rate index (ISDA's Floating Rate Option). However, non-standard offset calculation rules may apply for a trade if mutually agreed by the principal parties to the transaction.
  """
  initialFixingDate: Optional[InitialFixingDate] = Field(None, description="The initial fixing date.")
  """
  The initial fixing date.
  """
  rateCutOffDaysOffset: Optional[Offset] = Field(None, description="Specifies the number of business days before the period end date when the rate cut-off date is assumed to apply. The financial business centers associated with determining the rate cut-off date are those specified in the reset dates adjustments. The rate cut-off number of days must be a negative integer (a value of zero would imply no rate cut off applies in which case the rateCutOffDaysOffset element should not be included). The relevant rate for each reset date in the period from, and including, a rate cut-off date to, but excluding, the next applicable period end date (or, in the case of the last calculation period, the termination date) will (solely for purposes of calculating the floating amount payable on the next applicable payment date) be deemed to be the relevant rate in effect on that rate cut-off date. For example, if rate cut-off days for a daily averaging deal is -2 business days, then the refix rate applied on (period end date - 2 days) will also be applied as the reset on (period end date - 1 day), i.e. the actual number of reset dates remains the same but from the rate cut-off date until the period end date, the same refix rate is applied. Note that in the case of several calculation periods contributing to a single payment, the rate cut-off is assumed only to apply to the final calculation period contributing to that payment. The day type associated with the offset must imply a business days offset.")
  """
  Specifies the number of business days before the period end date when the rate cut-off date is assumed to apply. The financial business centers associated with determining the rate cut-off date are those specified in the reset dates adjustments. The rate cut-off number of days must be a negative integer (a value of zero would imply no rate cut off applies in which case the rateCutOffDaysOffset element should not be included). The relevant rate for each reset date in the period from, and including, a rate cut-off date to, but excluding, the next applicable period end date (or, in the case of the last calculation period, the termination date) will (solely for purposes of calculating the floating amount payable on the next applicable payment date) be deemed to be the relevant rate in effect on that rate cut-off date. For example, if rate cut-off days for a daily averaging deal is -2 business days, then the refix rate applied on (period end date - 2 days) will also be applied as the reset on (period end date - 1 day), i.e. the actual number of reset dates remains the same but from the rate cut-off date until the period end date, the same refix rate is applied. Note that in the case of several calculation periods contributing to a single payment, the rate cut-off is assumed only to apply to the final calculation period contributing to that payment. The day type associated with the offset must imply a business days offset.
  """
  resetDatesAdjustments: Optional[BusinessDayAdjustments] = Field(None, description="The definition of the business day convention and financial business centers used for adjusting the reset date if it would otherwise fall on a day that is not a business day in the specified business center.")
  """
  The definition of the business day convention and financial business centers used for adjusting the reset date if it would otherwise fall on a day that is not a business day in the specified business center.
  """
  resetFrequency: Optional[ResetFrequency] = Field(None, description="The frequency at which the reset dates occur. In the case of a weekly reset frequency, also specifies the day of the week that the reset occurs. If the reset frequency is greater than the calculation period frequency then this implies that more than one reset is established for each calculation period and some form of rate averaging is applicable.")
  """
  The frequency at which the reset dates occur. In the case of a weekly reset frequency, also specifies the day of the week that the reset occurs. If the reset frequency is greater than the calculation period frequency then this implies that more than one reset is established for each calculation period and some form of rate averaging is applicable.
  """
  resetRelativeTo: Optional[ResetRelativeToEnum] = Field(None, description="Specifies whether the reset dates are determined with respect to each adjusted calculation period start date or adjusted calculation period end date. If the reset frequency is specified as daily this element must not be included.")
  """
  Specifies whether the reset dates are determined with respect to each adjusted calculation period start date or adjusted calculation period end date. If the reset frequency is specified as daily this element must not be included.
  """
  
  @rosetta_condition
  def condition_0_RateCutOffDaysOffset(self):
    """
    FpML specifies that the rate cut-off number of days must be a negative integer with a value of zero would implying that no rate cut off applies, in which case the rateCutOffDaysOffset element should not be included.
    """
    def _then_fn0():
      return all_elements(self.rateCutOffDaysOffset.periodMultiplier, "<", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.rateCutOffDaysOffset) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_WeeklyPeriod(self):
    """
    FpML specifies that the weeklyRollConvention must be specified as part of the reset frequency if and only if the reset frequency is defined as weekly. This data rule is focused on the first part of the assertion.
    """
    def _then_fn0():
      return ((self.resetFrequency.weeklyRollConvention) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.resetFrequency.period, "=", PeriodExtendedEnum.W), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_NonWeeklyPeriod(self):
    """
    FpML specifies that the weeklyRollConvention must be specified as part of the reset frequency if and only if the reset frequency is defined as weekly. This data rule is focused on the latter part of the assertion.
    """
    def _then_fn0():
      return ((self.resetFrequency.weeklyRollConvention) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.resetFrequency.period, "<>", PeriodExtendedEnum.W), _then_fn0, _else_fn0)

from cdm.product.common.schedule.CalculationPeriodDates import CalculationPeriodDates
from cdm.base.datetime.AdjustableDate import AdjustableDate
from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset
from cdm.product.common.schedule.InitialFixingDate import InitialFixingDate
from cdm.base.datetime.Offset import Offset
from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments
from cdm.product.common.schedule.ResetFrequency import ResetFrequency
from cdm.product.common.schedule.ResetRelativeToEnum import ResetRelativeToEnum
from cdm.base.datetime.PeriodExtendedEnum import PeriodExtendedEnum

ResetDates.update_forward_refs()
