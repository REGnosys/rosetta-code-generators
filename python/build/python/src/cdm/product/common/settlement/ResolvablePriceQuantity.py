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

__all__ = ['ResolvablePriceQuantity']


class ResolvablePriceQuantity(BaseDataClass):
  """
  Generic class to specify the quantity for different payout legs in a contractual product, when that quantity can vary across payout legs or across time. A resolvable quantity can always be resolved into a single quantity from the quantity notation which has a corresponding asset identifier. In addition to the base case, where quantity is directly specified as a number as part of the quantity notation, the other use cases are: (i) quantity based on some pre-defined schedule (eg amortising notional), (ii) quantity based on some pre-defined events (eg resetting cross-currency notional), or quantity set as reference to another quantity (eg equity notional as no. securities x price).
  """
  futureValueNotional: Optional[FutureValueAmount] = Field(None, description="The future value notional is specific to BRL CDI swaps, and is specified alongside the notional amount. The value is calculated as follows: Future Value Notional = Notional Amount * (1 + Fixed Rate) ^ (Fixed Rate Day Count Fraction). The currency should always match that expressed in the notional schedule. The value date should match the adjusted termination date.")
  """
  The future value notional is specific to BRL CDI swaps, and is specified alongside the notional amount. The value is calculated as follows: Future Value Notional = Notional Amount * (1 + Fixed Rate) ^ (Fixed Rate Day Count Fraction). The currency should always match that expressed in the notional schedule. The value date should match the adjusted termination date.
  """
  priceSchedule: List[AttributeWithAddress[PriceSchedule] | PriceSchedule] = Field([], description="A payout's price specified as a schedule, which may also contain a single value if that price is constant. There may be multiple prices specified for a single payout: e.g. a floating interest rate leg may specify a spread, a cap and/or floor and a multiplier. The price must be specified outside of the payout in a PriceQuantity object and only referenced inside the payout using an address.")
  """
  A payout's price specified as a schedule, which may also contain a single value if that price is constant. There may be multiple prices specified for a single payout: e.g. a floating interest rate leg may specify a spread, a cap and/or floor and a multiplier. The price must be specified outside of the payout in a PriceQuantity object and only referenced inside the payout using an address.
  """
  quantityMultiplier: Optional[QuantityMultiplier] = Field(None, description="Quantity multiplier is specified on top of a reference quantity and is used as a multiplying factor when resolving the quantity. A quantity multiplier can only exist when the resolvable quantity specifies a reference quantity.")
  """
  Quantity multiplier is specified on top of a reference quantity and is used as a multiplying factor when resolving the quantity. A quantity multiplier can only exist when the resolvable quantity specifies a reference quantity.
  """
  quantityReference: Optional[AttributeWithReference | ResolvablePriceQuantity] = Field(None, description="Reference quantity when resolvable quantity is defined as relative to another (resolvable) quantity. A resolvable quantity needs to contain either an absolute quantity or a reference to another (resolvable) quantity. This requirement is captured by a choice rule on the class.")
  """
  Reference quantity when resolvable quantity is defined as relative to another (resolvable) quantity. A resolvable quantity needs to contain either an absolute quantity or a reference to another (resolvable) quantity. This requirement is captured by a choice rule on the class.
  """
  quantitySchedule: Optional[AttributeWithAddress[NonNegativeQuantitySchedule] | NonNegativeQuantitySchedule] = Field(None, description="A payout's quantity specified as a schedule, which may also contain a single value if that quantity is constant. There can only be a single quantity schedule applicable to a payout: e.g. the notional for an interest rate leg. The quantity must be specified outside of the payout in a PriceQuantity object and only referenced inside the payout using an address.")
  """
  A payout's quantity specified as a schedule, which may also contain a single value if that quantity is constant. There can only be a single quantity schedule applicable to a payout: e.g. the notional for an interest rate leg. The quantity must be specified outside of the payout in a PriceQuantity object and only referenced inside the payout using an address.
  """
  reset: Optional[bool] = Field(None, description="Whether the quantity is resettable")
  """
  Whether the quantity is resettable
  """
  resolvedQuantity: Optional[Quantity] = Field(None, description="A product's quantity as a single, non-negative amount.  When specified as part of a product definition, this quantity attribute would not be set.  Instead it is specified on the quantity notation along with an asset identifier matching this payout's asset identifier.  This allows the quantity to be resolved for a payout leg, which can then be specified here for convenience during data processing.  There needs to be at least one resolvable quantity across payout legs of a product to define an anchor that other payout quantities can refer to.  This attribute is ignored when mapping existing FpML messages.")
  """
  A product's quantity as a single, non-negative amount.  When specified as part of a product definition, this quantity attribute would not be set.  Instead it is specified on the quantity notation along with an asset identifier matching this payout's asset identifier.  This allows the quantity to be resolved for a payout leg, which can then be specified here for convenience during data processing.  There needs to be at least one resolvable quantity across payout legs of a product to define an anchor that other payout quantities can refer to.  This attribute is ignored when mapping existing FpML messages.
  """
  
  @rosetta_condition
  def condition_0_QuantityMultiplier(self):
    """
    A quantity reference must exist when there is a quantity multiplier on a resolvable quantity.
    """
    def _then_fn0():
      return ((ResolvablePriceQuantity.quantityReference.reference) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.quantityMultiplier) is not None), _then_fn0, _else_fn0)

from cdm.product.asset.FutureValueAmount import FutureValueAmount
from cdm.observable.asset.PriceSchedule import PriceSchedule
from cdm.product.common.settlement.QuantityMultiplier import QuantityMultiplier
from cdm.product.common.settlement.ResolvablePriceQuantity import ResolvablePriceQuantity
from cdm.base.math.NonNegativeQuantitySchedule import NonNegativeQuantitySchedule
from cdm.base.math.Quantity import Quantity

ResolvablePriceQuantity.update_forward_refs()
