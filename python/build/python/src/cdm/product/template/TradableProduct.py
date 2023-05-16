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

__all__ = ['TradableProduct']


class TradableProduct(BaseDataClass):
  """
  Definition of a product as ready to be traded, i.e. included in an execution or contract, by associating a specific price and quantity to this product plus an (optional) mechanism for any potential future quantity adjustment.
  """
  adjustment: Optional[NotionalAdjustmentEnum] = Field(None, description="Specifies the conditions that govern the adjustment to the quantity of a product being traded: e.g. execution, portfolio rebalancing etc. It is typically used in the context of Equity Swaps.")
  """
  Specifies the conditions that govern the adjustment to the quantity of a product being traded: e.g. execution, portfolio rebalancing etc. It is typically used in the context of Equity Swaps.
  """
  ancillaryParty: List[AncillaryParty] = Field([], description="Specifies the parties with ancillary roles in the transaction. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and this AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference.")
  """
  Specifies the parties with ancillary roles in the transaction. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and this AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference.
  """
  counterparty: List[Counterparty] = Field([], description="Specifies the parties which are the two counterparties to the transaction.  The product is agnostic to the actual parties to the transaction, with the party references abstracted away from the product definition and replaced by the counterparty enum (e.g. CounterpartyEnum values Party1 or Party2). The counterparty enum can then be positioned in the product (e.g. to specify which counterparty is the payer, receiver etc) and this counterparties attribute, which is positioned outside of the product definition, allows the counterparty enum to be associated with an actual party reference.")
  """
  Specifies the parties which are the two counterparties to the transaction.  The product is agnostic to the actual parties to the transaction, with the party references abstracted away from the product definition and replaced by the counterparty enum (e.g. CounterpartyEnum values Party1 or Party2). The counterparty enum can then be positioned in the product (e.g. to specify which counterparty is the payer, receiver etc) and this counterparties attribute, which is positioned outside of the product definition, allows the counterparty enum to be associated with an actual party reference.
  """
  @rosetta_condition
  def cardinality_counterparty(self):
    return check_cardinality(self.counterparty, 2, 2)
  
  product: Product = Field(..., description="The underlying product to be included in a contract or execution.")
  """
  The underlying product to be included in a contract or execution.
  """
  tradeLot: List[TradeLot] = Field([], description="Specifies the price, quantity and effective date of each trade lot, when the same product may be traded multiple times in different lots with the same counterparty. In a trade increase, a new trade lot is added to the list, with the corresponding effective date. In a trade decrease, the existing trade lot(s) are decreased of the corresponding quantity (and an unwind fee may have to be settled). The multiple cardinality and the ability to increase existing trades is used for Equity Swaps in particular.")
  """
  Specifies the price, quantity and effective date of each trade lot, when the same product may be traded multiple times in different lots with the same counterparty. In a trade increase, a new trade lot is added to the list, with the corresponding effective date. In a trade decrease, the existing trade lot(s) are decreased of the corresponding quantity (and an unwind fee may have to be settled). The multiple cardinality and the ability to increase existing trades is used for Equity Swaps in particular.
  """
  @rosetta_condition
  def cardinality_tradeLot(self):
    return check_cardinality(self.tradeLot, 1, None)
  
  
  @rosetta_condition
  def condition_0_PriceQuantityTriangulation(self):
    """
    Check PriceQuantity triangulation for each TradeLot.
    """
    return all_elements(PriceQuantityTriangulation(self.tradeLot), "=", False)
  
  @rosetta_condition
  def condition_1_NotionalAdjustment(self):
    """
    As the adjustment attribute applies to return swaps, the equity payout needs to be present alongside it.
    """
    def _then_fn0():
      return (((self.product.contractualProduct.economicTerms.payout.performancePayout.returnTerms.priceReturnTerms) is not None) or ((self.product.contractualProduct.economicTerms.payout.performancePayout) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.adjustment) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_DisruptionEventsDeterminingParty(self):
    def _then_fn1():
      return ((self.product.contractualProduct.economicTerms.extraordinaryEvents.additionalDisruptionEvents.determiningParty) is not None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (contains(self.ancillaryParty.role, AncillaryRoleEnum.DISRUPTION_EVENTS_DETERMINING_PARTY) and if_cond_fn(contains(self.ancillaryParty.role, AncillaryRoleEnum.DISRUPTION_EVENTS_DETERMINING_PARTY), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.extraordinaryEvents.additionalDisruptionEvents.determiningParty) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_PerformancePayout_ExtraordinaryDividendsParty(self):
    def _then_fn1():
      return ((self.product.contractualProduct.economicTerms.payout.performancePayout.returnTerms.dividendReturnTerms.extraordinaryDividendsParty) is not None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (contains(self.ancillaryParty.role, AncillaryRoleEnum.EXTRAORDINARY_DIVIDENDS_PARTY) and if_cond_fn(contains(self.ancillaryParty.role, AncillaryRoleEnum.EXTRAORDINARY_DIVIDENDS_PARTY), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.payout.performancePayout.returnTerms.dividendReturnTerms) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_OptionPayout_PredeterminedClearingOrganizationParty(self):
    def _then_fn0():
      return contains(self.ancillaryParty.role, AncillaryRoleEnum.PREDETERMINED_CLEARING_ORGANIZATION_PARTY)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.payout.optionPayout.settlementTerms.physicalSettlementTerms.predeterminedClearingOrganizationParty) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_5_ForwardPayout_PredeterminedClearingOrganizationParty(self):
    def _then_fn0():
      return contains(self.ancillaryParty.role, AncillaryRoleEnum.PREDETERMINED_CLEARING_ORGANIZATION_PARTY)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.payout.forwardPayout.settlementTerms.physicalSettlementTerms.predeterminedClearingOrganizationParty) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_6_PredeterminedClearingOrganizationParty(self):
    def _then_fn0():
      return (((self.product.contractualProduct.economicTerms.payout.forwardPayout.settlementTerms.physicalSettlementTerms.predeterminedClearingOrganizationParty) is not None) or ((self.product.contractualProduct.economicTerms.payout.optionPayout.settlementTerms.physicalSettlementTerms.predeterminedClearingOrganizationParty) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(contains(self.ancillaryParty.role, AncillaryRoleEnum.PREDETERMINED_CLEARING_ORGANIZATION_PARTY), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_7_ExerciseNoticeReceiverPartyManual(self):
    def _then_fn1():
      return ((self.product.contractualProduct.economicTerms.payout.optionPayout.exerciseTerms.exerciseProcedure.manualExercise.exerciseNotice.exerciseNoticeReceiver) is not None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (contains(self.ancillaryParty.role, AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_MANUAL) and if_cond_fn(contains(self.ancillaryParty.role, AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_MANUAL), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.payout.optionPayout.exerciseTerms.exerciseProcedure.manualExercise.exerciseNotice.exerciseNoticeReceiver) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_8_ExerciseNoticeReceiverPartyOptionalEarlyTermination(self):
    def _then_fn1():
      return ((self.product.contractualProduct.economicTerms.terminationProvision.earlyTerminationProvision.optionalEarlyTermination.exerciseNotice.exerciseNoticeReceiver) is not None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (contains(self.ancillaryParty.role, AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_OPTIONAL_EARLY_TERMINATION) and if_cond_fn(contains(self.ancillaryParty.role, AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_OPTIONAL_EARLY_TERMINATION), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.terminationProvision.earlyTerminationProvision.optionalEarlyTermination.exerciseNotice.exerciseNoticeReceiver) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_9_ExerciseNoticeReceiverPartyCancelableProvision(self):
    def _then_fn1():
      return ((self.product.contractualProduct.economicTerms.terminationProvision.cancelableProvision.exerciseNotice.exerciseNoticeReceiver) is not None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (contains(self.ancillaryParty.role, AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_CANCELABLE_PROVISION) and if_cond_fn(contains(self.ancillaryParty.role, AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_CANCELABLE_PROVISION), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.terminationProvision.cancelableProvision.exerciseNotice.exerciseNoticeReceiver) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_10_ExerciseNoticeReceiverPartyExtendibleProvision(self):
    def _then_fn1():
      return ((self.product.contractualProduct.economicTerms.terminationProvision.extendibleProvision.exerciseNotice.exerciseNoticeReceiver) is not None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (contains(self.ancillaryParty.role, AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_EXTENDIBLE_PROVISION) and if_cond_fn(contains(self.ancillaryParty.role, AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_EXTENDIBLE_PROVISION), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.terminationProvision.extendibleProvision.exerciseNotice.exerciseNoticeReceiver) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_11_CalculationAgentIndependent(self):
    def _then_fn1():
      return ((self.product.contractualProduct.economicTerms.calculationAgent.calculationAgentParty) is not None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (contains(self.ancillaryParty.role, AncillaryRoleEnum.CALCULATION_AGENT_INDEPENDENT) and if_cond_fn(contains(self.ancillaryParty.role, AncillaryRoleEnum.CALCULATION_AGENT_INDEPENDENT), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.calculationAgent.calculationAgentParty) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_12_CalculationAgentOptionalEarlyTermination(self):
    def _then_fn1():
      return ((self.product.contractualProduct.economicTerms.terminationProvision.earlyTerminationProvision.optionalEarlyTermination.calculationAgent.calculationAgentParty) is not None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (contains(self.ancillaryParty.role, AncillaryRoleEnum.CALCULATION_AGENT_OPTIONAL_EARLY_TERMINATION) and if_cond_fn(contains(self.ancillaryParty.role, AncillaryRoleEnum.CALCULATION_AGENT_OPTIONAL_EARLY_TERMINATION), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.terminationProvision.earlyTerminationProvision.optionalEarlyTermination.calculationAgent.calculationAgentParty) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_13_CalculationAgentMandatoryEarlyTermination(self):
    def _then_fn1():
      return ((self.product.contractualProduct.economicTerms.terminationProvision.earlyTerminationProvision.mandatoryEarlyTermination.calculationAgent.calculationAgentParty) is not None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (contains(self.ancillaryParty.role, AncillaryRoleEnum.CALCULATION_AGENT_MANDATORY_EARLY_TERMINATION) and if_cond_fn(contains(self.ancillaryParty.role, AncillaryRoleEnum.CALCULATION_AGENT_MANDATORY_EARLY_TERMINATION), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.product.contractualProduct.economicTerms.terminationProvision.earlyTerminationProvision.mandatoryEarlyTermination.calculationAgent.calculationAgentParty) is not None), _then_fn0, _else_fn0)

from cdm.product.common.NotionalAdjustmentEnum import NotionalAdjustmentEnum
from cdm.base.staticdata.party.AncillaryParty import AncillaryParty
from cdm.base.staticdata.party.Counterparty import Counterparty
from cdm.product.template.Product import Product
from cdm.product.template.TradeLot import TradeLot
from cdm.product.template.functions.PriceQuantityTriangulation import PriceQuantityTriangulation
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

TradableProduct.update_forward_refs()
