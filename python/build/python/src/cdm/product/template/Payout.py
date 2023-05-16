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

__all__ = ['Payout']


class Payout(BaseDataClass):
  """
  A class to represent the set of future cashflow methodologies in the form of specific payout class(es) that can be associated for the purpose of specifying a financial product. For example, two interest rate payouts can be combined to specify an interest rate swap, or one interest rate payout can be combined with a credit default payout to specify a credit default swap.
  """
  cashflow: List[Cashflow] = Field([], description="A cashflow between the parties to the trade. For interest rate and equity products, this corresponds to the FpML additionalPayment element. For credit default swaps, this corresponds to the FpML initialPayment element and the singlePayment element of the fee leg. For option products, it represents the FpML premium element.")
  """
  A cashflow between the parties to the trade. For interest rate and equity products, this corresponds to the FpML additionalPayment element. For credit default swaps, this corresponds to the FpML initialPayment element and the singlePayment element of the fee leg. For option products, it represents the FpML premium element.
  """
  commodityPayout: List[CommodityPayout] = Field([], description="Defines the payout for the floating leg of a Commodity Swap.")
  """
  Defines the payout for the floating leg of a Commodity Swap.
  """
  creditDefaultPayout: Optional[CreditDefaultPayout] = Field(None, description="The credit default payout, which provides the details necessary for determining when a credit payout will be triggered as well as the parameters for calculating the payout and the settlement terms.")
  """
  The credit default payout, which provides the details necessary for determining when a credit payout will be triggered as well as the parameters for calculating the payout and the settlement terms.
  """
  fixedPricePayout: List[FixedPricePayout] = Field([], description="Defines a payout in which one or more payouts are defined as a fixed price.")
  """
  Defines a payout in which one or more payouts are defined as a fixed price.
  """
  forwardPayout: List[ForwardPayout] = Field([], description="Represents a forward settling payout. The 'Underlier' attribute captures the underlying payout, which is settled according to the 'SettlementTerms' attribute. Both FX Spot and FX Forward should use this component.")
  """
  Represents a forward settling payout. The 'Underlier' attribute captures the underlying payout, which is settled according to the 'SettlementTerms' attribute. Both FX Spot and FX Forward should use this component.
  """
  interestRatePayout: List[InterestRatePayout] = Field([], description="All of the terms necessary to define and calculate a cash flow based on a fixed, a floating or an inflation index rate. The interest rate payout can be applied to interest rate swaps and FRA (which both have two associated interest rate payouts), credit default swaps (to represent the fee leg when subject to periodic payments) and equity swaps (to represent the funding leg).")
  """
  All of the terms necessary to define and calculate a cash flow based on a fixed, a floating or an inflation index rate. The interest rate payout can be applied to interest rate swaps and FRA (which both have two associated interest rate payouts), credit default swaps (to represent the fee leg when subject to periodic payments) and equity swaps (to represent the funding leg).
  """
  optionPayout: List[OptionPayout] = Field([], description="The option payout.")
  """
  The option payout.
  """
  performancePayout: List[PerformancePayout] = Field([], description="The performance payout, which encompasses the equity price returns, dividend returns, volatility return, variance return and correlation provisions.")
  """
  The performance payout, which encompasses the equity price returns, dividend returns, volatility return, variance return and correlation provisions.
  """
  securityFinancePayout: List[SecurityFinancePayout] = Field([], description="The security payout when the product involves some form of securities, such as collateral in a securities financing transaction")
  """
  The security payout when the product involves some form of securities, such as collateral in a securities financing transaction
  """
  securityPayout: List[SecurityPayout] = Field([], description="The security payout when the product involves some form of securities, such as collateral in a securities financing transaction")
  """
  The security payout when the product involves some form of securities, such as collateral in a securities financing transaction
  """
  
  @rosetta_condition
  def condition_0_ReturnType_Total_Requires_Dividends(self):
    """
    A total return implies both a price and a dividend return
    """
    def _then_fn0():
      return ((self.performancePayout.returnTerms.dividendReturnTerms) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.performancePayout.returnTerms.priceReturnTerms.returnType, "=", ReturnTypeEnum.TOTAL), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_LastRegularPaymentDate(self):
    """
    FpML specifies that lastRegularPaymentDate must only be included if there is a final stub. As part of the CDM, this data rule has been adjusted to specify that it only applies to interest rate swaps, as the credit derivatives products can have a specified lastRegularPaymentDate while the stub is typically not applicable to those.
    """
    def _then_fn0():
      return all_elements(len(self.interestRatePayout), "=", 2)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.interestRatePayout.paymentDates.lastRegularPaymentDate) is not None) and ((self.interestRatePayout.stubPeriod.finalStub) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_PayRelativeTo(self):
    """
    FpML specifies a required payRelativeTo element as part of the PaymentDates. As standardized CDS don't have such payRelativeTo provision, the cardinality has been relaxed as part of the CDM. This data rule specifies that if the product has two interest rate streams, this provision must exist.
    """
    def _then_fn0():
      return ((self.interestRatePayout.paymentDates.payRelativeTo) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((all_elements(len(self.interestRatePayout), "=", 2) and ((self.interestRatePayout.paymentDates) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_PaymentDatesAdjustments(self):
    """
    FpML specifies a required paymentDatesAdjustments element as part of the PaymentDates. As standardized CDS don't have such paymentDatesAdjustments provision, the cardinality has been relaxed as part of the CDM. This data rule specifies that if the product has two interest rate streams, this provision must exist.
    """
    def _then_fn0():
      return ((self.interestRatePayout.paymentDates.paymentDatesAdjustments) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((all_elements(len(self.interestRatePayout), "=", 2) and ((self.interestRatePayout.paymentDates) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_PaymentFrequency(self):
    """
    FpML specifies a required paymentFrequency element as part of the PaymentDates. As standardized CDS may not have such paymentFrequency provision, the cardinality has been relaxed as part of the CDM. This data rule specifies that if the product has two interest rate streams, this provision must exist.
    """
    def _then_fn0():
      return ((self.interestRatePayout.paymentDates.paymentFrequency) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((all_elements(len(self.interestRatePayout), "=", 2) and ((self.interestRatePayout.paymentDates) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_5_Quantity(self):
    """
    When there is an OptionPayout the quantity can be expressed as part of the payoutQuantity, or as part of the underlier in the case of a Swaption.  For all other payouts that extend PayoutBase the payoutQuantity is a mandatory attribute.
    """
    def _then_fn0():
      return (((self.optionPayout.priceQuantity) is not None) or all_elements(len(self.optionPayout.underlier.contractualProduct.economicTerms.payout.interestRatePayout), "=", 2))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.optionPayout) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_6_DayCountFraction(self):
    """
    FpML specifies a required dayCountFraction element as part of the swapStream/calculationPeriodAmount/calculation. As standardized CDS don't have such specified day count fraction, the cardinality has been relaxed as part of the CDM. This data rule specifies that if the product has two interest rate streams, this provision must exist.
    """
    def _then_fn0():
      return ((self.interestRatePayout.dayCountFraction) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(len(self.interestRatePayout), "=", 2), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_7_PaymentDates(self):
    """
    FpML specifies a required paymentDates element as part of the swapStream. As standardized CDS may not have specified payment dates, the cardinality has been relaxed as part of the CDM. This data rule specifies that if the product has two interest rate streams, this provision must exist.
    """
    def _then_fn0():
      return ((self.interestRatePayout.dayCountFraction) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(len(self.interestRatePayout), "=", 2), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_8_MarketPrice(self):
    """
    FpML specifies that marketFixedRate and marketPrice only have meaning in a credit index trade
    """
    def _then_fn0():
      return (((self.creditDefaultPayout.transactedPrice.marketFixedRate) is None) and ((self.creditDefaultPayout.transactedPrice.marketPrice) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.creditDefaultPayout.generalTerms.indexReferenceInformation) is None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_9_NotionalResetOnPerformancePayout(self):
    """
    Notional reset only applies to return swaps, and therefore can only exist on an performancePayout.
    """
    return (((((self.interestRatePayout.priceQuantity.reset) is None) and ((self.creditDefaultPayout.priceQuantity.reset) is None)) and ((self.optionPayout.priceQuantity.reset) is None)) and ((self.cashflow.priceQuantity.reset) is None))
  
  @rosetta_condition
  def condition_10_NotionalResetInterestRatePayoutExists(self):
    """
    As the performancePayout->payoutQuantity->reset attribute applies to return swaps, the interestRatePayout needs to be present alongside it.
    """
    def _then_fn0():
      return ((self.interestRatePayout) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(contains(self.performancePayout.priceQuantity.reset, False), _then_fn0, _else_fn0)

from cdm.product.common.settlement.Cashflow import Cashflow
from cdm.product.asset.CommodityPayout import CommodityPayout
from cdm.product.asset.CreditDefaultPayout import CreditDefaultPayout
from cdm.product.template.FixedPricePayout import FixedPricePayout
from cdm.product.template.ForwardPayout import ForwardPayout
from cdm.product.asset.InterestRatePayout import InterestRatePayout
from cdm.product.template.OptionPayout import OptionPayout
from cdm.product.template.PerformancePayout import PerformancePayout
from cdm.product.template.SecurityFinancePayout import SecurityFinancePayout
from cdm.product.template.SecurityPayout import SecurityPayout
from cdm.product.asset.ReturnTypeEnum import ReturnTypeEnum

Payout.update_forward_refs()
