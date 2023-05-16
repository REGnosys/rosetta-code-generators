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

__all__ = ['FixedPricePayout']

from cdm.product.common.settlement.PayoutBase import PayoutBase

class FixedPricePayout(PayoutBase):
  """
  Represents a fixed price payout. There is no underlier associated with this payout type and is based on fixed pricing per a given unit (e.g. in commodities price per barrel)
  """
  fixedPrice: FixedPrice = Field(..., description="Specifies the fixed price on which fixed forward payments are based.")
  """
  Specifies the fixed price on which fixed forward payments are based.
  """
  paymentDates: PaymentDates = Field(..., description="Specifies the parameters to generate the payment date schedule, either through a parametric representation or by reference to specified dates.")
  """
  Specifies the parameters to generate the payment date schedule, either through a parametric representation or by reference to specified dates.
  """
  schedule: Optional[CommoditySchedule] = Field(None, description="Allows the full representation of a commodity payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.")
  """
  Allows the full representation of a commodity payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.
  """
  
  @rosetta_condition
  def condition_0_Quantity(self):
    """
    When there is an OptionPayout the quantity can be expressed as part of the payoutQuantity, or as part of the underlier in the case of a Swaption.  For all other payouts that extend PayoutBase the payoutQuantity is a mandatory attribute.
    """
    return ((self.priceQuantity) is not None)

from cdm.product.common.settlement.FixedPrice import FixedPrice
from cdm.product.common.schedule.PaymentDates import PaymentDates
from cdm.product.template.CommoditySchedule import CommoditySchedule

FixedPricePayout.update_forward_refs()
