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

__all__ = ['PerformancePayout']

from cdm.product.common.settlement.PayoutBase import PayoutBase

class PerformancePayout(PayoutBase):
  """
  Contains the necessary specifications for all performance payouts, encompassing equity return, dividend, variance, volatility and correlation products.
  """
  fxFeature: List[FxFeature] = Field([], description="Defines quanto or composite FX features that are included in the swap leg.")
  """
  Defines quanto or composite FX features that are included in the swap leg.
  """
  observationTerms: Optional[ObservationTerms] = Field(None, description="Defines how and when a performance type option or performance type swap is to be observed.")
  """
  Defines how and when a performance type option or performance type swap is to be observed.
  """
  paymentDates: PaymentDates = Field(..., description="Defines the payment date schedule, as defined by the parameters that are needed to specify it, either in a parametric way or by reference to another schedule of dates (e.g. the valuation dates).")
  """
  Defines the payment date schedule, as defined by the parameters that are needed to specify it, either in a parametric way or by reference to another schedule of dates (e.g. the valuation dates).
  """
  returnTerms: ReturnTerms = Field(..., description="Specifies the type of return of a performance payout.")
  """
  Specifies the type of return of a performance payout.
  """
  underlier: Optional[Product] = Field(None, description="Identifies the underlying product that is referenced for pricing of the applicable leg in a swap.  Referenced in the '2018 ISDA CDM Equity Confirmation for Security Equity Swap' as Security.")
  """
  Identifies the underlying product that is referenced for pricing of the applicable leg in a swap.  Referenced in the '2018 ISDA CDM Equity Confirmation for Security Equity Swap' as Security.
  """
  valuationDates: ValuationDates = Field(..., description="Defines how and when a performance type option or performance type swap is to be valued, including both interim and final valuation.")
  """
  Defines how and when a performance type option or performance type swap is to be valued, including both interim and final valuation.
  """
  
  @rosetta_condition
  def condition_0_Quantity(self):
    """
    When there is an OptionPayout the quantity can be expressed as part of the payoutQuantity, or as part of the underlier in the case of a Swaption.  For all other payouts that extend PayoutBase the payoutQuantity is a mandatory attribute.
    """
    return ((self.priceQuantity) is not None)
  
  @rosetta_condition
  def condition_1_NoSharePriceDividendAdjustmentIndex(self):
    """
    If the underlier is an index, sharePriceAdjustment and sharePriceDividendAdjustment cannot exist.
    """
    def _then_fn0():
      return (((self.returnTerms.varianceReturnTerms.sharePriceDividendAdjustment) is None) and ((self.returnTerms.volatilityReturnTerms.sharePriceDividendAdjustment) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.underlier.index) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_NoSharePriceDividendAdjustmentForeignExchange(self):
    """
    If the underlier is an foreign exchange, sharePriceAdjustment and sharePriceDividendAdjustment cannot exist.
    """
    def _then_fn0():
      return (((self.returnTerms.varianceReturnTerms.sharePriceDividendAdjustment) is None) and ((self.returnTerms.volatilityReturnTerms.sharePriceDividendAdjustment) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.underlier.foreignExchange) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_CorrelationUnderlierOnlyBasket(self):
    """
    Correlation Return Terms can only have a basket as underlier, since it needs to compute the correlation between two or more products.
    """
    def _then_fn0():
      return self.check_one_of_constraint(self, self.underlier.basket)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.returnTerms.correlationReturnTerms) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_EquitySpecificAttributes(self):
    """
    Equity specific attributes cannot be present in non-equity products.
    """
    def _then_fn0():
      return ((((((((((self.returnTerms.varianceReturnTerms.dividendApplicability) is None) and ((self.returnTerms.varianceReturnTerms.equityUnderlierProvisions) is None)) and ((self.returnTerms.varianceReturnTerms.sharePriceDividendAdjustment) is None)) and ((self.returnTerms.volatilityReturnTerms.dividendApplicability) is None)) and ((self.returnTerms.volatilityReturnTerms.equityUnderlierProvisions) is None)) and ((self.returnTerms.volatilityReturnTerms.sharePriceDividendAdjustment) is None)) and ((self.returnTerms.correlationReturnTerms.dividendApplicability) is None)) and ((self.returnTerms.correlationReturnTerms.equityUnderlierProvisions) is None)) and ((self.returnTerms.correlationReturnTerms.sharePriceDividendAdjustment) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(Qualify_AssetClass_Equity(self.underlier), "=", False), _then_fn0, _else_fn0)

from cdm.product.template.FxFeature import FxFeature
from cdm.product.common.schedule.ObservationTerms import ObservationTerms
from cdm.product.common.schedule.PaymentDates import PaymentDates
from cdm.product.template.ReturnTerms import ReturnTerms
from cdm.product.template.Product import Product
from cdm.observable.asset.ValuationDates import ValuationDates
from cdm.product.qualification.functions.Qualify_AssetClass_Equity import Qualify_AssetClass_Equity

PerformancePayout.update_forward_refs()
