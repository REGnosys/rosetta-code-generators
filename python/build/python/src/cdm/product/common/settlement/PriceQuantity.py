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

__all__ = ['PriceQuantity']


class PriceQuantity(BaseDataClass):
  """
  Defines a settlement as an exchange between two parties of a specified quantity of an asset (the quantity) against a specified quantity of another asset (the price). The settlement is optional and can be either cash or physical. In the case of non-cash products, the settlement of the price/quantity would not be specified here and instead would be delegated to the product mechanics, as parameterised by the price/quantity values.
  """
  buyerSeller: Optional[BuyerSeller] = Field(None, description="Defines the direction of the exchange. The convention is that the buyer receives the quantity / pays the price, whereas the seller receives the price / pays the quantity. Attribute is optional in case the price/quantity settlement is defined as part of the product mechanics.")
  """
  Defines the direction of the exchange. The convention is that the buyer receives the quantity / pays the price, whereas the seller receives the price / pays the quantity. Attribute is optional in case the price/quantity settlement is defined as part of the product mechanics.
  """
  effectiveDate: Optional[AdjustableOrRelativeDate] = Field(None, description="Specifies the date at which the price and quantity become effective. This day may be subject to adjustment in accordance with a business day convention, or could be specified as relative to a trade date, for instance. Optional cardinality, as the effective date is usually specified in the product definition, so it may only need to be specified as part of the PriceQuantity in an increase/decrease scenario for an existing trade.")
  """
  Specifies the date at which the price and quantity become effective. This day may be subject to adjustment in accordance with a business day convention, or could be specified as relative to a trade date, for instance. Optional cardinality, as the effective date is usually specified in the product definition, so it may only need to be specified as part of the PriceQuantity in an increase/decrease scenario for an existing trade.
  """
  observable: Optional[Observable] = Field(None, description="Specifies the object to be observed for a price, it could be an asset or a reference. The cardinality is optional as some quantity / price cases have no observable (e.g. a notional and a fixed rate in a given currency).")
  """
  Specifies the object to be observed for a price, it could be an asset or a reference. The cardinality is optional as some quantity / price cases have no observable (e.g. a notional and a fixed rate in a given currency).
  """
  price: List[AttributeWithMeta[PriceSchedule] | PriceSchedule] = Field([], description="Specifies a price to be used for trade amounts and other purposes.")
  """
  Specifies a price to be used for trade amounts and other purposes.
  """
  quantity: List[AttributeWithMeta[NonNegativeQuantitySchedule] | NonNegativeQuantitySchedule] = Field([], description="Specifies a quantity to be associated with an event, for example a trade amount.")
  """
  Specifies a quantity to be associated with an event, for example a trade amount.
  """
  settlementTerms: Optional[SettlementTerms] = Field(None, description="Whether the settlement is cash or physical and the corresponding terms. Attribute is optional in case the price/quantity settlement is defined as part of the product mechanics.")
  """
  Whether the settlement is cash or physical and the corresponding terms. Attribute is optional in case the price/quantity settlement is defined as part of the product mechanics.
  """
  
  @rosetta_condition
  def condition_0_RateOptionObservable(self):
    """
    When the observable is a rate option, the price type must correspond to one of the interest rate price expressions.
    """
    def _then_fn0():
      return (contains(self.price.priceExpression.priceType, PriceTypeEnum.INTEREST_RATE) or contains(self.price.priceExpression.priceType, PriceTypeEnum.MULTIPLIER_OF_INDEX_VALUE))
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.observable.rateOption) is not None) and ((self.price) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_ActualSettlement(self):
    """
    Settlement terms must be present when the settlement direction is specified.
    """
    def _then_fn0():
      return ((self.settlementTerms) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.buyerSeller) is not None), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.BuyerSeller import BuyerSeller
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.observable.asset.Observable import Observable
from cdm.observable.asset.PriceSchedule import PriceSchedule
from cdm.base.math.NonNegativeQuantitySchedule import NonNegativeQuantitySchedule
from cdm.product.common.settlement.SettlementTerms import SettlementTerms
from cdm.observable.asset.PriceTypeEnum import PriceTypeEnum

PriceQuantity.update_forward_refs()
