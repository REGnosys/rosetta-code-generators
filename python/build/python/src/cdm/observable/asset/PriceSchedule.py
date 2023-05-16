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

__all__ = ['PriceSchedule']

from cdm.base.math.MeasureSchedule import MeasureSchedule

class PriceSchedule(MeasureSchedule):
  """
  Specifies the price of a financial instrument in a trade as a schedule of measures. A price generically expresses the value of an exchange as a ratio: it measures the amount of one thing needed to be exchanged for 1 unit of another thing (e.g. cash in a specific currency in exchange for a bond or share). This generic representation can be used to support any type of financial price beyond just cash price: e.g. an interest rate, a foreign exchange rate, etc. This data type is generically based on a schedule and can also be used to represent a price as a single value.
  """
  perUnitOf: Optional[UnitType] = Field(None, description="Provides an attribute to define the unit of the thing being priced. For example, {amount, unitOfAmount, PerUnitOfAmount} = [10, EUR, Shares] = (10.00 EUR/SHARE) * (300,000 SHARES) = EUR 3,000,000.00 (Shares cancel out in the calculation).")
  """
  Provides an attribute to define the unit of the thing being priced. For example, {amount, unitOfAmount, PerUnitOfAmount} = [10, EUR, Shares] = (10.00 EUR/SHARE) * (300,000 SHARES) = EUR 3,000,000.00 (Shares cancel out in the calculation).
  """
  priceExpression: PriceExpression = Field(..., description="Provides a value for the type of price expression (cash price, interest rate, gross or net, clean or dirty etc.) in order to explain how to interpret the amount and use it in calculations.")
  """
  Provides a value for the type of price expression (cash price, interest rate, gross or net, clean or dirty etc.) in order to explain how to interpret the amount and use it in calculations.
  """
  
  @rosetta_condition
  def condition_0_UnitOfAmountExists(self):
    """
    Requires that a unit of amount must be specified for price unless price type is Variance, Volatility or Correlation.
    """
    def _then_fn0():
      return (((self.unit) is None) and ((self.perUnitOf) is None))
    
    def _else_fn0():
      return (((self.unit) is not None) and ((self.perUnitOf) is not None))
    
    return if_cond_fn(((all_elements(self.priceExpression.priceType, "=", PriceTypeEnum.VARIANCE) or all_elements(self.priceExpression.priceType, "=", PriceTypeEnum.VOLATILITY)) or all_elements(self.priceExpression.priceType, "=", PriceTypeEnum.CORRELATION)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_PositiveFXRate(self):
    """
    Requires that per FpML rules, the FX rate must be a positive value.
    """
    def _then_fn0():
      return all_elements(self.value, ">", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((all_elements(self.priceExpression.priceType, "=", PriceTypeEnum.EXCHANGE_RATE) or all_elements(self.priceExpression.priceType, "=", PriceTypeEnum.ASSET_PRICE)) and ((self.priceExpression.spreadType) is None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_PositiveSpotRate(self):
    """
    Requires that per FpML rules, the spot rate must be a positive value, for example for FX or Commodities.
    """
    def _then_fn0():
      return all_elements(self.value, ">", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((all_elements(self.priceExpression.priceType, "=", PriceTypeEnum.EXCHANGE_RATE) or all_elements(self.priceExpression.priceType, "=", PriceTypeEnum.ASSET_PRICE)) and all_elements(self.priceExpression.spreadType, "=", SpreadTypeEnum.BASE)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_PositiveCashPrice(self):
    """
    Requires that any price expressed as a cash price and generating a cashflow must be positive
    """
    def _then_fn0():
      return all_elements(self.value, ">", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.priceExpression.priceType, "=", PriceTypeEnum.CASH_PRICE), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_CurrencyUnitForInterestRate(self):
    """
    Requires that the unit of amount for an interest rate must be a currency.
    """
    def _then_fn0():
      return ((self.unit.currency) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.priceExpression.priceType, "=", PriceTypeEnum.INTEREST_RATE), _then_fn0, _else_fn0)

from cdm.base.math.UnitType import UnitType
from cdm.observable.asset.PriceExpression import PriceExpression
from cdm.observable.asset.PriceTypeEnum import PriceTypeEnum
from cdm.observable.asset.SpreadTypeEnum import SpreadTypeEnum

PriceSchedule.update_forward_refs()
