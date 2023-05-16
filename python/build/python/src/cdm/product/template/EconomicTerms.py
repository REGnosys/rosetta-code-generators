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

__all__ = ['EconomicTerms']


class EconomicTerms(BaseDataClass):
  """
   This class represents the full set of price-forming features associated with a contractual product: the payout component, the notional/quantity, the effective and termination date and the date adjustment provisions when applying uniformily across the payout components. This class also includes the legal provisions which have valuation implications: cancelable provision, extendible provision, early termination provision and extraordinary events specification.
  """
  calculationAgent: Optional[CalculationAgent] = Field(None, description="The ISDA calculation agent responsible for performing duties as defined in the applicable product definitions.")
  """
  The ISDA calculation agent responsible for performing duties as defined in the applicable product definitions.
  """
  dateAdjustments: Optional[BusinessDayAdjustments] = Field(None, description="The business day adjustment convention when it applies across all the payout components. This specification of the business day convention and financial business centers is used for adjusting any calculation period date if it would otherwise fall on a day that is not a business day in the specified business center.")
  """
  The business day adjustment convention when it applies across all the payout components. This specification of the business day convention and financial business centers is used for adjusting any calculation period date if it would otherwise fall on a day that is not a business day in the specified business center.
  """
  effectiveDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The first day of the terms of the trade. This day may be subject to adjustment in accordance with a business day convention.")
  """
  The first day of the terms of the trade. This day may be subject to adjustment in accordance with a business day convention.
  """
  extraordinaryEvents: Optional[ExtraordinaryEvents] = Field(None, description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Extraordinary Events.")
  """
  2018 ISDA CDM Equity Confirmation for Security Equity Swap: Extraordinary Events.
  """
  nonStandardisedTerms: Optional[bool] = Field(None, description="Specifies, when boolean value is True, that additional economic terms exist that have not been included in the product representation.")
  """
  Specifies, when boolean value is True, that additional economic terms exist that have not been included in the product representation.
  """
  payout: Payout = Field(..., description="The payout specifies the future cashflow computation methodology which characterizes a financial product.")
  """
  The payout specifies the future cashflow computation methodology which characterizes a financial product.
  """
  terminationDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The last day of the terms of the trade. This date may be subject to adjustments in accordance with the business day convention. It can also be specified in relation to another scheduled date (e.g. the last payment date).")
  """
  The last day of the terms of the trade. This date may be subject to adjustments in accordance with the business day convention. It can also be specified in relation to another scheduled date (e.g. the last payment date).
  """
  terminationProvision: Optional[TerminationProvision] = Field(None, description="Contains optional provisions pertaining to the termination characteristics of a contract.")
  """
  Contains optional provisions pertaining to the termination characteristics of a contract.
  """
  
  @rosetta_condition
  def condition_0_ExtraordinaryEvents(self):
    """
    Extraordinary events provisions must be associated with an equity payout.
    """
    def _then_fn0():
      return (((self.payout.performancePayout.returnTerms.priceReturnTerms) is not None) or ((self.payout.optionPayout.underlier.security) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.extraordinaryEvents) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_FpML_cd_26_28(self):
    """
    FpML validation rule cd-26 - If feeLeg/singlePayment/adjustablePaymentDate exists, then feeLeg/singlePayment/adjustablePaymentDate must be after generalTerms/effectiveDate/unadjustedDate. FpML validation rule cd-28 - If feeLeg/periodicPayment/firstPaymentDate exists, then feeLeg/periodicPayment/firstPaymentDate must be after generalTerms/effectiveDate/unadjustedDate. This data rule tackles those two FpML validation rules at once, as the singlePayment and the firstPayment have been represented through the same Payout/cashflow attribute.
    """
    def _then_fn0():
      return ((all_elements(self.payout.cashflow.settlementTerms.settlementDate.adjustableOrRelativeDate.unadjustedDate, ">", self.effectiveDate.adjustableDate.unadjustedDate) or all_elements(self.payout.cashflow.settlementTerms.settlementDate.adjustableOrRelativeDate.adjustedDate, ">", self.effectiveDate.adjustableDate.adjustedDate)) or all_elements(self.payout.cashflow.settlementTerms.settlementDate.adjustableOrRelativeDate.relativeDate.adjustedDate, ">", self.effectiveDate.relativeDate.adjustedDate))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((((((self.payout.creditDefaultPayout) is not None) and ((self.payout.cashflow) is not None)) and ((self.effectiveDate) is not None)) and ((self.payout.cashflow.settlementTerms.settlementDate.adjustableOrRelativeDate.unadjustedDate) is not None)) and ((self.payout.cashflow.settlementTerms.settlementDate.adjustableOrRelativeDate.relativeDate) is None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_FpML_cd_27(self):
    """
    FpML validation rule cd-27 - If feeLeg/singlePayment/adjustablePaymentDate exists, and if generalTerms/scheduledTerminationDate exists, then feeLeg/singlePayment/adjustablePaymentDate must be before generalTerms/scheduledTerminationDate/unadjustedDate.
    """
    def _then_fn0():
      return ((all_elements(self.payout.cashflow.settlementTerms.settlementDate.adjustableOrRelativeDate.unadjustedDate, "<", self.terminationDate.adjustableDate.unadjustedDate) or all_elements(self.payout.cashflow.settlementTerms.settlementDate.adjustableOrRelativeDate.adjustedDate, "<", self.terminationDate.adjustableDate.adjustedDate)) or all_elements(self.payout.cashflow.settlementTerms.settlementDate.adjustableOrRelativeDate.relativeDate.adjustedDate, "<", self.terminationDate.adjustableDate.adjustedDate))
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((((self.payout.creditDefaultPayout) is not None) and ((self.payout.cashflow) is not None)) and ((self.terminationDate) is not None)) and ((self.payout.cashflow.settlementTerms.settlementDate.adjustableOrRelativeDate) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_FpML_cd_30(self):
    """
    FpML validation rule cd-30 - If feeLeg/periodicPayment/lastRegularPaymentDate exists, and if generalTerms/scheduledTerminationDate exists, then feeLeg/periodicPayment/lastRegularPaymentDate must be before generalTerms/scheduledTerminationDate/unadjustedDate.
    """
    def _then_fn0():
      return all_elements(self.payout.interestRatePayout.paymentDates.lastRegularPaymentDate, "<", self.terminationDate.adjustableDate.unadjustedDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.payout.interestRatePayout.paymentDates.lastRegularPaymentDate) is not None) and ((self.terminationDate) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_IndependentCalculationAgent(self):
    def _then_fn0():
      return all_elements(self.calculationAgent.calculationAgentParty, "=", AncillaryRoleEnum.CALCULATION_AGENT_INDEPENDENT)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.calculationAgent.calculationAgentParty) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_5_SecurityFinancePayoutDividendTermsValidation(self):
    """
    Validates that if the transaction has Dividend Terms specified then it should be a Term trade.
    """
    def _then_fn0():
      return ((self.terminationDate) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.payout.securityFinancePayout.dividendTerms) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_6_ExtendibleProvisionExerciseDetails(self):
    """
    Ensure that the correct details are specified for an extendible contract.
    """
    def _then_fn1():
      return ((((((self.terminationProvision.extendibleProvision.americanExercise) is not None) and ((self.terminationProvision.extendibleProvision.bermudaExercise) is None)) and ((self.terminationProvision.extendibleProvision.europeanExercise) is None)) or ((((self.terminationProvision.extendibleProvision.americanExercise) is None) and ((self.terminationProvision.extendibleProvision.bermudaExercise) is not None)) and ((self.terminationProvision.extendibleProvision.europeanExercise) is None))) or (((((self.terminationProvision.extendibleProvision.americanExercise) is None) and ((self.terminationProvision.extendibleProvision.bermudaExercise) is None)) and ((self.terminationProvision.extendibleProvision.europeanExercise) is not None)) and ((self.terminationProvision.extendibleProvision.followUpConfirmation) is not None)))
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return if_cond_fn(((self.terminationProvision.extendibleProvision) is not None), _then_fn1, _else_fn1)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.payout.securityFinancePayout) is None), _then_fn0, _else_fn0)

from cdm.observable.asset.CalculationAgent import CalculationAgent
from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.observable.event.ExtraordinaryEvents import ExtraordinaryEvents
from cdm.product.template.Payout import Payout
from cdm.product.template.TerminationProvision import TerminationProvision
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

EconomicTerms.update_forward_refs()
