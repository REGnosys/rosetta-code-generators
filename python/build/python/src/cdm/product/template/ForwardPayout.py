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

__all__ = ['ForwardPayout']


class ForwardPayout(BaseDataClass):
  """
  Represents a forward settling payout. The 'Underlier' attribute captures the underlying payout, which is settled according to the 'SettlementTerms' attribute. Both FX Spot and FX Forward should use this component.
  """
  settlementTerms: SettlementTerms = Field(..., description="Settlement terms for the underlier that include the settlement date, settlement method etc.")
  """
  Settlement terms for the underlier that include the settlement date, settlement method etc.
  """
  underlier: Product = Field(..., description="Underlying product that the forward is written on, which can be of any type: FX, a contractual product, a security, etc.")
  """
  Underlying product that the forward is written on, which can be of any type: FX, a contractual product, a security, etc.
  """
  
  @rosetta_condition
  def condition_0_SettlementDate(self):
    """
    For foreign exchange contracts, either the settlementDate is set or the cashflowDates, but not both. When the cashflowDates are set, they must be the same for the 2 legs of the currency pair.
    """
    def _then_fn0():
      return (((((self.settlementTerms.settlementDate.valueDate) is not None) and ((self.underlier.foreignExchange.exchangedCurrency1.settlementTerms.settlementDate.adjustableOrRelativeDate) is None)) and ((self.underlier.foreignExchange.exchangedCurrency2.settlementTerms.settlementDate.adjustableOrRelativeDate) is None)) or (((((self.settlementTerms.settlementDate.valueDate) is None) and ((self.underlier.foreignExchange.exchangedCurrency1.settlementTerms.settlementDate.adjustableOrRelativeDate) is not None)) and ((self.underlier.foreignExchange.exchangedCurrency2.settlementTerms.settlementDate.adjustableOrRelativeDate) is not None)) and all_elements(self.underlier.foreignExchange.exchangedCurrency1.settlementTerms.settlementDate.adjustableOrRelativeDate, "=", self.underlier.foreignExchange.exchangedCurrency2.settlementTerms.settlementDate.adjustableOrRelativeDate)))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.underlier.foreignExchange) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_FxSettlement(self):
    """
    For foreign exchange contracts, the settlement type must be either fx non-deliverable settlement or not specified, which implies physical settlement in the case of foreign exchange.
    """
    def _then_fn0():
      return ((self.settlementTerms.physicalSettlementTerms) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.underlier.foreignExchange) is not None), _then_fn0, _else_fn0)

from cdm.product.common.settlement.SettlementTerms import SettlementTerms
from cdm.product.template.Product import Product

ForwardPayout.update_forward_refs()
