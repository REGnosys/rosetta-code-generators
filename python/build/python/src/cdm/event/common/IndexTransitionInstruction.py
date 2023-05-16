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

__all__ = ['IndexTransitionInstruction']


class IndexTransitionInstruction(BaseDataClass):
  """
  Defines the information needed to create a Index Transition Business Event.
  """
  cashTransfer: Optional[Transfer] = Field(None, description="Specifies the cash transfer that can optionally be tied to an index transition event.")
  """
  Specifies the cash transfer that can optionally be tied to an index transition event.
  """
  effectiveDate: date = Field(..., description="Specifies the effective date of the index transition event. This is first date on which the floating rate calculation will use the new floating rate index and adjusted spread in the floating rate calculation.")
  """
  Specifies the effective date of the index transition event. This is first date on which the floating rate calculation will use the new floating rate index and adjusted spread in the floating rate calculation.
  """
  priceQuantity: List[PriceQuantity] = Field([], description="Specifies both new floating rate index and spread adjustment for each leg to be updated.  The spread adjustment accounts for the difference between the old floating rate index relative to the new one. This spread amount is added to the existing spread to determine the new spread, which is applied from the specified effective date forward. In the case of the IBOR Fallback Rate Adjustments, the adjustment spread (also known as the Fallback Adjustment) accounts for two distinctions: i) the fact that the replacement Risk-Free Rate is an overnight rate while IBORs have term structures (e.g., 1, 3, 6-month LIBOR); and (ii) the historical spread differential between IBORs and their term equivalent Overnight Risk-Free Rate compounded rates.")
  """
  Specifies both new floating rate index and spread adjustment for each leg to be updated.  The spread adjustment accounts for the difference between the old floating rate index relative to the new one. This spread amount is added to the existing spread to determine the new spread, which is applied from the specified effective date forward. In the case of the IBOR Fallback Rate Adjustments, the adjustment spread (also known as the Fallback Adjustment) accounts for two distinctions: i) the fact that the replacement Risk-Free Rate is an overnight rate while IBORs have term structures (e.g., 1, 3, 6-month LIBOR); and (ii) the historical spread differential between IBORs and their term equivalent Overnight Risk-Free Rate compounded rates.
  """
  @rosetta_condition
  def cardinality_priceQuantity(self):
    return check_cardinality(self.priceQuantity, 1, None)
  
  
  @rosetta_condition
  def condition_0_PriceQuantity(self):
    return ((contains(self.priceQuantity.price.priceExpression.priceType, PriceTypeEnum.INTEREST_RATE) and ((self.priceQuantity.observable.rateOption) is not None)) and ((self.priceQuantity.quantity) is None))

from cdm.event.common.Transfer import Transfer
from cdm.product.common.settlement.PriceQuantity import PriceQuantity
from cdm.observable.asset.PriceTypeEnum import PriceTypeEnum

IndexTransitionInstruction.update_forward_refs()
