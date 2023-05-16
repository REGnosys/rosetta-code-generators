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

__all__ = ['CommodityPayout']

from cdm.product.common.settlement.PayoutBase import PayoutBase

class CommodityPayout(PayoutBase):
  """
  Payout based on the averaged price of a referenced underlier. (e.g. Commodities). Can represent both average (average of many) & bullet (average of 1) pricing
  """
  averagingFeature: Optional[AveragingCalculation] = Field(None, description="Indicates if the averaging calculation, when applicable, is weighted or unweighted.")
  """
  Indicates if the averaging calculation, when applicable, is weighted or unweighted.
  """
  calculationPeriodDates: Optional[CalculationPeriodDates] = Field(None, description="Defines the calculation period dates schedule.")
  """
  Defines the calculation period dates schedule.
  """
  commodityPriceReturnTerms: Optional[CommodityPriceReturnTerms] = Field(None, description="Defines parameters in which the commodity price is assessed.")
  """
  Defines parameters in which the commodity price is assessed.
  """
  fxFeature: Optional[FxFeature] = Field(None, description="Defines quanto or composite FX features that are included in the swap leg.")
  """
  Defines quanto or composite FX features that are included in the swap leg.
  """
  paymentDates: PaymentDates = Field(..., description="Defines the payment date schedule, as defined by the parameters that are needed to specify it, either in a parametric way or by reference to another schedule of dates (e.g. the valuation dates).")
  """
  Defines the payment date schedule, as defined by the parameters that are needed to specify it, either in a parametric way or by reference to another schedule of dates (e.g. the valuation dates).
  """
  pricingDates: PricingDates = Field(..., description="Specifies specific dates or parametric rules for the dates on which the price will be determined.")
  """
  Specifies specific dates or parametric rules for the dates on which the price will be determined.
  """
  schedule: Optional[CommoditySchedule] = Field(None, description="Allows the full representation of a commodity payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.")
  """
  Allows the full representation of a commodity payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.
  """
  underlier: Product = Field(..., description="Identifies the underlying product that is referenced for pricing of the applicable leg in a swap.  Referenced in the '2018 ISDA CDM Equity Confirmation for Security Equity Swap' as Security.")
  """
  Identifies the underlying product that is referenced for pricing of the applicable leg in a swap.  Referenced in the '2018 ISDA CDM Equity Confirmation for Security Equity Swap' as Security.
  """
  
  @rosetta_condition
  def condition_0_Quantity(self):
    """
    When there is an OptionPayout the quantity can be expressed as part of the payoutQuantity, or as part of the underlier in the case of a Swaption.  For all other payouts that extend PayoutBase the payoutQuantity is a mandatory attribute.
    """
    return ((self.priceQuantity) is not None)
  
  @rosetta_condition
  def condition_1_CalculationPeriod(self):
    """
    The calculation periods are either specified parametrically via CalculationPeriodDates or non-parametrically via SchedulePeriod.
    """
    return self.check_one_of_constraint('schedule', 'calculationPeriodDates', necessity=True)

from cdm.product.template.AveragingCalculation import AveragingCalculation
from cdm.product.common.schedule.CalculationPeriodDates import CalculationPeriodDates
from cdm.product.common.settlement.CommodityPriceReturnTerms import CommodityPriceReturnTerms
from cdm.product.template.FxFeature import FxFeature
from cdm.product.common.schedule.PaymentDates import PaymentDates
from cdm.product.common.settlement.PricingDates import PricingDates
from cdm.product.template.CommoditySchedule import CommoditySchedule
from cdm.product.template.Product import Product

CommodityPayout.update_forward_refs()
