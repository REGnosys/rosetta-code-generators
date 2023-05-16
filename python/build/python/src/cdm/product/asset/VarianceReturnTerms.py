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

__all__ = ['VarianceReturnTerms']

from cdm.product.asset.ReturnTermsBase import ReturnTermsBase

class VarianceReturnTerms(ReturnTermsBase):
  exchangeTradedContractNearest: Optional[Observable] = Field(None, description="Specification of the exchange traded contract nearest.")
  """
  Specification of the exchange traded contract nearest.
  """
  varianceCapFloor: Optional[VarianceCapFloor] = Field(None, description="Contains possible barriers for variance products, both variance-based and underlier price based")
  """
  Contains possible barriers for variance products, both variance-based and underlier price based
  """
  varianceStrikePrice: Optional[Price] = Field(None, description="Variance Strike Price in accordance with the ISDA 2011 Equity Derivatives Definitions.")
  """
  Variance Strike Price in accordance with the ISDA 2011 Equity Derivatives Definitions.
  """
  vegaNotionalAmount: Optional[NonNegativeQuantitySchedule] = Field(None, description="Vega Notional represents the approximate gain/loss at maturity for a 1% difference between RVol (realised vol) and KVol (strike vol). It does not necessarily represent the Vega Risk of the trade.")
  """
  Vega Notional represents the approximate gain/loss at maturity for a 1% difference between RVol (realised vol) and KVol (strike vol). It does not necessarily represent the Vega Risk of the trade.
  """
  volatilityCapFloor: Optional[VolatilityCapFloor] = Field(None, description="Contains containing volatility-based barriers")
  """
  Contains containing volatility-based barriers
  """
  volatilityStrikePrice: Optional[Price] = Field(None, description="Volatility Strike Price in accordance with the ISDA 2011 Equity Derivatives Definitions.")
  """
  Volatility Strike Price in accordance with the ISDA 2011 Equity Derivatives Definitions.
  """
  
  @rosetta_condition
  def condition_0_Positive_VegaNotionalAmount(self):
    """
    When the optional vegaNotionalAmount is present in the varianceReturnTerms, it needs to have a positive value.
    """
    def _then_fn0():
      return all_elements(self.vegaNotionalAmount.value, ">", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.vegaNotionalAmount.value) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_UnderlierMustBeSecurity(self):
    """
    If an exchange traded contract nearest is specified, it must have a security as underlier.
    """
    def _then_fn0():
      return ((self.exchangeTradedContractNearest.productIdentifier) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.exchangeTradedContractNearest) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_ReferenceContract(self):
    """
    If futurePriceValuation is true, an exchange traded contract is used as a reference, therefore such contract must be specified in exchangeTradedContractNearest
    """
    def _then_fn0():
      return ((self.exchangeTradedContractNearest) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.valuation.futuresPriceValuation, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_StrikePriceMustExist(self):
    """
    The strike price must be present, but it can be expressed in either variance or volatility terms
    """
    return self.check_one_of_constraint('volatilityStrikePrice', 'varianceStrikePrice', necessity=True)
  
  @rosetta_condition
  def condition_4_NonNegativeStrikePrice(self):
    """
    The strike price must have a positive value
    """
    def _then_fn1():
      return all_elements(self.varianceStrikePrice.value, ">=", 0)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (all_elements(self.volatilityStrikePrice.value, ">=", 0) and if_cond_fn(((self.varianceStrikePrice.value) is not None), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.volatilityStrikePrice.value) is not None), _then_fn0, _else_fn0)

from cdm.observable.asset.Observable import Observable
from cdm.product.asset.VarianceCapFloor import VarianceCapFloor
from cdm.observable.asset.Price import Price
from cdm.base.math.NonNegativeQuantitySchedule import NonNegativeQuantitySchedule
from cdm.product.asset.VolatilityCapFloor import VolatilityCapFloor

VarianceReturnTerms.update_forward_refs()
