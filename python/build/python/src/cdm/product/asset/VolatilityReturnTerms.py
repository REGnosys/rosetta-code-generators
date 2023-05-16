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

__all__ = ['VolatilityReturnTerms']

from cdm.product.asset.ReturnTermsBase import ReturnTermsBase

class VolatilityReturnTerms(ReturnTermsBase):
  exchangeTradedContractNearest: Optional[Observable] = Field(None, description="Specification of the exchange traded contract nearest.")
  """
  Specification of the exchange traded contract nearest.
  """
  volatilityCapFloor: Optional[VolatilityCapFloor] = Field(None, description="Contains volatility-based barriers")
  """
  Contains volatility-based barriers
  """
  volatilityStrikePrice: Price = Field(..., description="Volatility Strike Price in accordance with the ISDA 2011 Equity Derivatives Definitions.")
  """
  Volatility Strike Price in accordance with the ISDA 2011 Equity Derivatives Definitions.
  """
  
  @rosetta_condition
  def condition_0_UnderlierMustBeSecurity(self):
    """
    If an exchange traded contract nearest is specified, it must have a security as underlier.
    """
    def _then_fn0():
      return ((self.exchangeTradedContractNearest.productIdentifier) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.exchangeTradedContractNearest) is not None), _then_fn0, _else_fn0)

from cdm.observable.asset.Observable import Observable
from cdm.product.asset.VolatilityCapFloor import VolatilityCapFloor
from cdm.observable.asset.Price import Price

VolatilityReturnTerms.update_forward_refs()
