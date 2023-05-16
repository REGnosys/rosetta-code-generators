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

__all__ = ['ReturnTerms']


class ReturnTerms(BaseDataClass):
  """
  Specifies the type of return of a performance payout.
  """
  correlationReturnTerms: Optional[CorrelationReturnTerms] = Field(None, description="Return terms based upon the observed correlation between the components of the underlying basket.")
  """
  Return terms based upon the observed correlation between the components of the underlying basket.
  """
  dividendReturnTerms: Optional[DividendReturnTerms] = Field(None, description="Return terms based upon dividend payments associated to the underlier.")
  """
  Return terms based upon dividend payments associated to the underlier.
  """
  priceReturnTerms: Optional[PriceReturnTerms] = Field(None, description="Return terms based upon the underlier's observed price.")
  """
  Return terms based upon the underlier's observed price.
  """
  varianceReturnTerms: Optional[VarianceReturnTerms] = Field(None, description="Return terms based upon the observed variance of the underlier's price.")
  """
  Return terms based upon the observed variance of the underlier's price.
  """
  volatilityReturnTerms: Optional[VolatilityReturnTerms] = Field(None, description="Return terms based upon the observed volatility of the underlier's price.")
  """
  Return terms based upon the observed volatility of the underlier's price.
  """
  
  @rosetta_condition
  def condition_0_ReturnTermsExists(self):
    """
    Checks that the return type label matches the actual return terms structure of the product.
    """
    def _then_fn1():
      return self.check_one_of_constraint(self, self.priceReturnTerms)
    
    def _else_fn1():
      return ((((self.check_one_of_constraint(self, self.priceReturnTerms) or self.check_one_of_constraint(self, self.dividendReturnTerms)) or self.check_one_of_constraint(self, self.varianceReturnTerms)) or self.check_one_of_constraint(self, self.volatilityReturnTerms)) or self.check_one_of_constraint(self, self.correlationReturnTerms))
    
    def _then_fn0():
      return self.check_one_of_constraint(self, self.priceReturnTerms)
    
    def _else_fn0():
      return if_cond_fn(all_elements(self.priceReturnTerms.returnType, "=", ReturnTypeEnum.PRICE), _then_fn1, _else_fn1)
    
    return if_cond_fn(all_elements(self.priceReturnTerms.returnType, "=", ReturnTypeEnum.TOTAL), _then_fn0, _else_fn0)

from cdm.product.asset.CorrelationReturnTerms import CorrelationReturnTerms
from cdm.product.asset.DividendReturnTerms import DividendReturnTerms
from cdm.product.asset.PriceReturnTerms import PriceReturnTerms
from cdm.product.asset.VarianceReturnTerms import VarianceReturnTerms
from cdm.product.asset.VolatilityReturnTerms import VolatilityReturnTerms
from cdm.product.asset.ReturnTypeEnum import ReturnTypeEnum

ReturnTerms.update_forward_refs()
