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

__all__ = ['PaymentDates']


class PaymentDates(BaseDataClass):
  """
  Specifies the parameters to generate the payment date schedule, either through a parametric representation or by reference to specified dates.
  """
  firstPaymentDate: Optional[date] = Field(None, description="The first unadjusted payment date. This day may be subject to adjustment in accordance with any business day convention specified in paymentDatesAdjustments. This element must only be included if there is an initial stub. This date will normally correspond to an unadjusted calculation period start or end date. This is true even if early or delayed payment is specified to be applicable since the actual first payment date will be the specified number of days before or after the applicable adjusted calculation period start or end date with the resulting payment date then being adjusted in accordance with any business day convention specified in paymentDatesAdjustments.")
  """
  The first unadjusted payment date. This day may be subject to adjustment in accordance with any business day convention specified in paymentDatesAdjustments. This element must only be included if there is an initial stub. This date will normally correspond to an unadjusted calculation period start or end date. This is true even if early or delayed payment is specified to be applicable since the actual first payment date will be the specified number of days before or after the applicable adjusted calculation period start or end date with the resulting payment date then being adjusted in accordance with any business day convention specified in paymentDatesAdjustments.
  """
  lastRegularPaymentDate: Optional[date] = Field(None, description="The last regular payment date when specified as a date, as in the FpML interest rate construct. FpML specifies that this date may be subject to adjustment in accordance with any business day convention specified in the paymentDatesAdjustments attribute.")
  """
  The last regular payment date when specified as a date, as in the FpML interest rate construct. FpML specifies that this date may be subject to adjustment in accordance with any business day convention specified in the paymentDatesAdjustments attribute.
  """
  payRelativeTo: Optional[PayRelativeToEnum] = Field(None, description="Specifies whether the payments occur relative to each adjusted calculation period start date or end date, each reset date, valuation date or the last pricing date. Calculation period start date means relative to the start of the first calculation period contributing to a given payment. Similarly, calculation period end date means the end of the last calculation period contributing to a given payment. The valuation date is applicable for Brazilian-CDI and equity swaps.")
  """
  Specifies whether the payments occur relative to each adjusted calculation period start date or end date, each reset date, valuation date or the last pricing date. Calculation period start date means relative to the start of the first calculation period contributing to a given payment. Similarly, calculation period end date means the end of the last calculation period contributing to a given payment. The valuation date is applicable for Brazilian-CDI and equity swaps.
  """
  paymentDateSchedule: Optional[PaymentDateSchedule] = Field(None, description="The payment dates when specified as relative to a set of dates specified somewhere else in the instance document/transaction, e.g. the valuation dates as typically the case for equity swaps, or when specified as a calculation period schedule.")
  """
  The payment dates when specified as relative to a set of dates specified somewhere else in the instance document/transaction, e.g. the valuation dates as typically the case for equity swaps, or when specified as a calculation period schedule.
  """
  paymentDatesAdjustments: Optional[BusinessDayAdjustments] = Field(None, description="The definition of the business day convention and financial business centers used for adjusting the payment date if it would otherwise fall on a day that is not a business day in the specified business center.")
  """
  The definition of the business day convention and financial business centers used for adjusting the payment date if it would otherwise fall on a day that is not a business day in the specified business center.
  """
  paymentDaysOffset: Optional[Offset] = Field(None, description="If early payment or delayed payment is required, specifies the number of days offset that the payment occurs relative to what would otherwise be the unadjusted payment date. The offset can be specified in terms of either calendar or business days. Even in the case of a calendar days offset, the resulting payment date, adjusted for the specified calendar days offset, will still be adjusted in accordance with the specified payment dates adjustments. This element should only be included if early or delayed payment is applicable, i.e. if the periodMultiplier element value is not equal to zero. An early payment would be indicated by a negative periodMultiplier element value and a delayed payment (or payment lag) would be indicated by a positive periodMultiplier element value.")
  """
  If early payment or delayed payment is required, specifies the number of days offset that the payment occurs relative to what would otherwise be the unadjusted payment date. The offset can be specified in terms of either calendar or business days. Even in the case of a calendar days offset, the resulting payment date, adjusted for the specified calendar days offset, will still be adjusted in accordance with the specified payment dates adjustments. This element should only be included if early or delayed payment is applicable, i.e. if the periodMultiplier element value is not equal to zero. An early payment would be indicated by a negative periodMultiplier element value and a delayed payment (or payment lag) would be indicated by a positive periodMultiplier element value.
  """
  paymentFrequency: Optional[Frequency] = Field(None, description="The frequency at which regular payment dates occur. If the payment frequency is equal to the frequency defined in the calculation period dates component then one calculation period contributes to each payment amount. If the payment frequency is less frequent than the frequency defined in the calculation period dates component then more than one calculation period will contribute to the payment amount. A payment frequency more frequent than the calculation period frequency or one that is not a multiple of the calculation period frequency is invalid. If the payment frequency is of value T (term), the period is defined by the effectiveDate and the terminationDate.")
  """
  The frequency at which regular payment dates occur. If the payment frequency is equal to the frequency defined in the calculation period dates component then one calculation period contributes to each payment amount. If the payment frequency is less frequent than the frequency defined in the calculation period dates component then more than one calculation period will contribute to the payment amount. A payment frequency more frequent than the calculation period frequency or one that is not a multiple of the calculation period frequency is invalid. If the payment frequency is of value T (term), the period is defined by the effectiveDate and the terminationDate.
  """
  
  @rosetta_condition
  def condition_0_FpML_ird_35_cd_31(self):
    """
    FpML validation rule ird-35 & cd-31- If firstPaymentDate exists, and if lastRegularPaymentDate exists, then firstPaymentDate must be before lastRegularPaymentDate.
    """
    def _then_fn0():
      return all_elements(self.firstPaymentDate, "<", self.lastRegularPaymentDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.firstPaymentDate) is not None) and ((self.lastRegularPaymentDate) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_NonZeroPeriodMultiplier(self):
    """
    FpML specifies that paymentDaysOffset should only be included if early or delayed payment is applicable, i.e. if the periodMultiplier element value is not equal to zero.
    """
    def _then_fn0():
      return any_elements(self.paymentDaysOffset.periodMultiplier, "<>", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.paymentDaysOffset) is not None), _then_fn0, _else_fn0)

from cdm.product.common.schedule.PayRelativeToEnum import PayRelativeToEnum
from cdm.product.common.schedule.PaymentDateSchedule import PaymentDateSchedule
from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments
from cdm.base.datetime.Offset import Offset
from cdm.base.datetime.Frequency import Frequency

PaymentDates.update_forward_refs()
