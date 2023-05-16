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

__all__ = ['PriceExpression']


class PriceExpression(BaseDataClass):
  capFloor: Optional[CapFloorEnum] = Field(None, description="")
  cashPrice: Optional[CashPrice] = Field(None, description="")
  cleanOrDirty: Optional[CleanOrDirtyPriceEnum] = Field(None, description="")
  grossOrNet: Optional[GrossOrNetEnum] = Field(None, description="")
  priceExpression: Optional[PriceExpressionEnum] = Field(None, description="")
  priceType: PriceTypeEnum = Field(..., description="")
  spreadType: Optional[SpreadTypeEnum] = Field(None, description="")
  
  @rosetta_condition
  def condition_0_Choice(self):
    """
    The price can be specified mutually exclusively as a cashflow, an interest rate, or clean/dirty (in case it's a bond price).
    """
    return self.check_one_of_constraint('cashPrice', 'cleanOrDirty', 'capFloor', necessity=False)
  
  @rosetta_condition
  def condition_1_CashPrice(self):
    """
    If a cash price type is specified, the price type must be cash.
    """
    def _then_fn0():
      return all_elements(self.priceType, "=", PriceTypeEnum.CASH_PRICE)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.cashPrice) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_CleanOrDirty(self):
    """
    Clean or dirty indicator only applicable for asset (bond) price.
    """
    def _then_fn0():
      return all_elements(self.priceType, "=", PriceTypeEnum.ASSET_PRICE)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.cleanOrDirty) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_CapFloorPrice(self):
    """
    Cap / Floor type can only be specified when the price type is a rate price.
    """
    def _then_fn0():
      return all_elements(self.priceType, "=", PriceTypeEnum.INTEREST_RATE)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.capFloor) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_SpreadPrice(self):
    """
    A spread type can only be specified when the price type is an asset price, an exchange rate or an interest rate.
    """
    def _then_fn0():
      return ((all_elements(self.priceType, "=", PriceTypeEnum.ASSET_PRICE) or all_elements(self.priceType, "=", PriceTypeEnum.EXCHANGE_RATE)) or all_elements(self.priceType, "=", PriceTypeEnum.INTEREST_RATE))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.spreadType) is not None), _then_fn0, _else_fn0)

from cdm.observable.asset.CapFloorEnum import CapFloorEnum
from cdm.observable.asset.CashPrice import CashPrice
from cdm.observable.asset.CleanOrDirtyPriceEnum import CleanOrDirtyPriceEnum
from cdm.observable.asset.GrossOrNetEnum import GrossOrNetEnum
from cdm.observable.asset.PriceExpressionEnum import PriceExpressionEnum
from cdm.observable.asset.PriceTypeEnum import PriceTypeEnum
from cdm.observable.asset.SpreadTypeEnum import SpreadTypeEnum

PriceExpression.update_forward_refs()
