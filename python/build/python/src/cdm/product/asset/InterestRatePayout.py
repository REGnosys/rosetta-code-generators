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

__all__ = ['InterestRatePayout']

from cdm.product.common.settlement.PayoutBase import PayoutBase

class InterestRatePayout(PayoutBase):
  """
   A class to specify all of the terms necessary to define and calculate a cash flow based on a fixed, a floating or an inflation index rate. The interest rate payout can be applied to interest rate swaps and FRA (which both have two associated interest rate payouts), credit default swaps (to represent the fee leg when subject to periodic payments) and equity swaps (to represent the funding leg). The associated globalKey denotes the ability to associate a hash value to the InterestRatePayout instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.
  """
  bondReference: Optional[BondReference] = Field(None, description="Reference to a bond underlier to represent an asset swap or Condition Precedent Bond.")
  """
  Reference to a bond underlier to represent an asset swap or Condition Precedent Bond.
  """
  calculationPeriodDates: Optional[CalculationPeriodDates] = Field(None, description="The parameters used to generate the calculation period dates schedule, including the specification of any initial or final stub calculation periods.")
  """
  The parameters used to generate the calculation period dates schedule, including the specification of any initial or final stub calculation periods.
  """
  cashflowRepresentation: Optional[CashflowRepresentation] = Field(None, description="The cashflow representation of the swap stream.")
  """
  The cashflow representation of the swap stream.
  """
  compoundingMethod: Optional[CompoundingMethodEnum] = Field(None, description="If one or more calculation period contributes to a single payment amount this element specifies whether compounding is applicable and, if so, what compounding method is to be used. This element must only be included when more than one calculation period contributes to a single payment amount.")
  """
  If one or more calculation period contributes to a single payment amount this element specifies whether compounding is applicable and, if so, what compounding method is to be used. This element must only be included when more than one calculation period contributes to a single payment amount.
  """
  dayCountFraction: Optional[AttributeWithMeta[DayCountFractionEnum] | DayCountFractionEnum] = Field(None, description="The day count fraction. The cardinality has been relaxed when compared with the FpML interest rate swap for the purpose of accommodating standardized credit default swaps which DCF is not explicitly stated as part of the economic terms. The data rule InterestRatePayout_dayCountFraction requires that the DCF be stated for interest rate products.")
  """
  The day count fraction. The cardinality has been relaxed when compared with the FpML interest rate swap for the purpose of accommodating standardized credit default swaps which DCF is not explicitly stated as part of the economic terms. The data rule InterestRatePayout_dayCountFraction requires that the DCF be stated for interest rate products.
  """
  discountingMethod: Optional[DiscountingMethod] = Field(None, description="The parameters specifying any discounting conventions that may apply. This element must only be included if discounting applies.")
  """
  The parameters specifying any discounting conventions that may apply. This element must only be included if discounting applies.
  """
  fixedAmount: Optional[str] = Field(None, description="Fixed Amount Calculation")
  """
  Fixed Amount Calculation
  """
  floatingAmount: Optional[str] = Field(None, description="Floating Amount Calculation")
  """
  Floating Amount Calculation
  """
  paymentDate: Optional[AdjustableDate] = Field(None, description="The payment date, where only one date is specified, as for the FRA product.")
  """
  The payment date, where only one date is specified, as for the FRA product.
  """
  paymentDates: Optional[PaymentDates] = Field(None, description="The payment date schedule, as defined by the parameters that are needed to specify it, either in a parametric way or by reference to another schedule of dates (e.g. the reset dates).")
  """
  The payment date schedule, as defined by the parameters that are needed to specify it, either in a parametric way or by reference to another schedule of dates (e.g. the reset dates).
  """
  paymentDelay: Optional[bool] = Field(None, description="Applicable to CDS on MBS to specify whether payment delays are applicable to the fixed Amount. RMBS typically have a payment delay of 5 days between the coupon date of the reference obligation and the payment date of the synthetic swap. CMBS do not, on the other hand, with both payment dates being on the 25th of each month.")
  """
  Applicable to CDS on MBS to specify whether payment delays are applicable to the fixed Amount. RMBS typically have a payment delay of 5 days between the coupon date of the reference obligation and the payment date of the synthetic swap. CMBS do not, on the other hand, with both payment dates being on the 25th of each month.
  """
  rateSpecification: Optional[RateSpecification] = Field(None, description="The specification of the rate value(s) applicable to the contract using either a floating rate calculation, a single fixed rate, a fixed rate schedule, or an inflation rate calculation.")
  """
  The specification of the rate value(s) applicable to the contract using either a floating rate calculation, a single fixed rate, a fixed rate schedule, or an inflation rate calculation.
  """
  resetDates: Optional[ResetDates] = Field(None, description="The reset dates schedule, i.e. the dates on which the new observed index value is applied for each period and the interest rate hence begins to accrue.")
  """
  The reset dates schedule, i.e. the dates on which the new observed index value is applied for each period and the interest rate hence begins to accrue.
  """
  stubPeriod: Optional[StubPeriod] = Field(None, description="The stub calculation period amount parameters. This element must only be included if there is an initial or final stub calculation period. Even then, it must only be included if either the stub references a different floating rate tenor to the regular calculation periods, or if the stub is calculated as a linear interpolation of two different floating rate tenors, or if a specific stub rate or stub amount has been negotiated.")
  """
  The stub calculation period amount parameters. This element must only be included if there is an initial or final stub calculation period. Even then, it must only be included if either the stub references a different floating rate tenor to the regular calculation periods, or if the stub is calculated as a linear interpolation of two different floating rate tenors, or if a specific stub rate or stub amount has been negotiated.
  """
  
  @rosetta_condition
  def condition_0_Quantity(self):
    """
    When there is an OptionPayout the quantity can be expressed as part of the payoutQuantity, or as part of the underlier in the case of a Swaption.  For all other payouts that extend PayoutBase the payoutQuantity is a mandatory attribute.
    """
    return ((self.priceQuantity) is not None)
  
  @rosetta_condition
  def condition_1_InterestRatePayoutChoice(self):
    """
    The paymentDates attributes is applicable to interest rate payouts with periodic payments, while the paymentDate reflects the FpML FRA implementation where one specific date is specified.
    """
    return self.check_one_of_constraint('paymentDates', 'paymentDate', necessity=False)
  
  @rosetta_condition
  def condition_2_FutureValueNotional(self):
    """
    The BRL CDI future value notional only applies to a fixed Rate Schedule.
    """
    def _then_fn0():
      return ((self.priceQuantity.futureValueNotional) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.rateSpecification.fixedRate) is None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_TerminationDate(self):
    """
    FpML states that the value date associated with the future value notional should match the adjusted termination date.
    """
    def _then_fn0():
      return all_elements(self.priceQuantity.futureValueNotional.valueDate, "=", self.calculationPeriodDates.terminationDate.adjustableDate.adjustedDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.priceQuantity.futureValueNotional) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_RateSpecification(self):
    def _then_fn0():
      return all_elements(self.principalPayment.finalPayment, "=", False)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.rateSpecification) is None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_5_FpML_ird_6(self):
    """
    FpML validation rule ird-6 - If paymentDates/firstPaymentDate exists, and if calculationPeriodDates/effectiveDate exists, then paymentDates/firstPaymentDate must be after calculationPeriodDates/effectiveDate/unadjustedDate.
    """
    def _then_fn0():
      return all_elements(self.paymentDates.firstPaymentDate, ">", self.calculationPeriodDates.effectiveDate.adjustableDate.unadjustedDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.paymentDates.firstPaymentDate) is not None) and ((self.calculationPeriodDates.effectiveDate) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_6_FpML_ird_23(self):
    """
    FpML validation rule ird-23 - If the initialStub exists, the calculationPeriodDates element referenced by the @href attribute of stubCalculationPeriodAmount/calculationPeriodDatesReference contains firstRegularPeriodStartDate.
    """
    def _then_fn0():
      return ((self.calculationPeriodDates.firstRegularPeriodStartDate) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.stubPeriod.initialStub) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_7_FpML_ird_24(self):
    """
    FpML validation rule ird-24 - The finalStub exists if and only if the calculationPeriodDates element referenced by calculationPeriodDates/@href contains a lastRegularPeriodEndDate.
    """
    def _then_fn0():
      return ((self.calculationPeriodDates.lastRegularPeriodEndDate) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.stubPeriod.finalStub) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_8_InitialStubFinalStub(self):
    """
    Data rule to represent the FpML nested XML construct as part of StubCalculationPeriodAmount.
    """
    def _then_fn0():
      return (((self.stubPeriod.initialStub) is not None) or ((self.stubPeriod.finalStub) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.stubPeriod) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_9_CashSettlementTerms(self):
    """
    Cash Settlements Terms must exist when the settlement currency is different to the notional currency of the trade.
    """
    def _then_fn0():
      return ((((self.settlementTerms.cashSettlementTerms.valuationMethod) is not None) and ((self.settlementTerms.cashSettlementTerms.valuationDate) is not None)) or ((self.priceQuantity.quantityMultiplier.fxLinkedNotionalSchedule.fxSpotRateSource) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.settlementTerms.settlementCurrency) is not None) and (any_elements(self.settlementTerms.settlementCurrency, "<>", self.priceQuantity.quantitySchedule.unit.currency) or any_elements(self.settlementTerms.settlementCurrency, "<>", self.priceQuantity.quantityMultiplier.fxLinkedNotionalSchedule.varyingNotionalCurrency))), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_10_FpML_ird_7_1(self):
    """
    FpML validation rule ird-7 1/2 - The existence of compoundingMethod is prohibited when the calculation period and payment frequencies are the same.
    """
    def _then_fn0():
      return (((self.compoundingMethod) is None) or all_elements(self.compoundingMethod, "=", CompoundingMethodEnum.NONE))
    
    def _else_fn0():
      return True
    
    return if_cond_fn((all_elements(self.paymentDates.paymentFrequency.period, "=", self.calculationPeriodDates.calculationPeriodFrequency.period) and all_elements(self.paymentDates.paymentFrequency.periodMultiplier, "=", self.calculationPeriodDates.calculationPeriodFrequency.periodMultiplier)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_11_FpML_ird_7_2(self):
    """
    FpML validation rule ird-7 2/2 - The existence of compoundingMethod is required when the calculation period and payment frequencies differ.
    """
    def _then_fn0():
      return ((self.compoundingMethod) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((((self.paymentDates.paymentFrequency.period) is not None) and ((self.calculationPeriodDates.calculationPeriodFrequency.period) is not None)) and any_elements(self.paymentDates.paymentFrequency.period, "<>", self.calculationPeriodDates.calculationPeriodFrequency.period)) or ((((self.paymentDates.paymentFrequency.periodMultiplier) is not None) and ((self.calculationPeriodDates.calculationPeriodFrequency.periodMultiplier) is not None)) and any_elements(self.paymentDates.paymentFrequency.periodMultiplier, "<>", self.calculationPeriodDates.calculationPeriodFrequency.periodMultiplier))), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_12_FpML_ird_9(self):
    """
    FpML validation rule ird-9 - If calculationPeriodAmount/calculation/compoundingMethod exists, then resetDates must exist.
    """
    def _then_fn0():
      return ((self.resetDates) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.compoundingMethod) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_13_FpML_ird_29(self):
    """
    FpML validation rule ird-29 - If compoundingMethod exists, then fixedRateSchedule must not exist.
    """
    def _then_fn0():
      return ((self.rateSpecification.fixedRate) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.compoundingMethod) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_14_CalculationPeriodDatesFirstCompoundingPeriodEndDate(self):
    """
    FpML specifies that the firstCompoundingPeriodEndDate must only be specified when the compounding method is specified and not equal to a value of None.
    """
    def _then_fn0():
      return ((self.calculationPeriodDates.firstCompoundingPeriodEndDate) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.compoundingMethod) is None) or all_elements(self.compoundingMethod, "=", CompoundingMethodEnum.NONE)), _then_fn0, _else_fn0)

from cdm.product.asset.BondReference import BondReference
from cdm.product.common.schedule.CalculationPeriodDates import CalculationPeriodDates
from cdm.product.asset.CashflowRepresentation import CashflowRepresentation
from cdm.product.asset.CompoundingMethodEnum import CompoundingMethodEnum
from cdm.base.datetime.daycount.DayCountFractionEnum import DayCountFractionEnum
from cdm.product.asset.DiscountingMethod import DiscountingMethod
from cdm.base.datetime.AdjustableDate import AdjustableDate
from cdm.product.common.schedule.PaymentDates import PaymentDates
from cdm.product.asset.RateSpecification import RateSpecification
from cdm.product.common.schedule.ResetDates import ResetDates
from cdm.product.common.schedule.StubPeriod import StubPeriod

InterestRatePayout.update_forward_refs()
