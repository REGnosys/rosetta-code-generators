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

__all__ = ['CrossRate']

from cdm.observable.asset.QuotedCurrencyPair import QuotedCurrencyPair

class CrossRate(QuotedCurrencyPair):
  """
  A class that is used for including the currency exchange rates used to cross between the traded currencies for non-base currency FX contracts.
  """
  forwardPoints: Optional[Decimal] = Field(None, description="An optional element used for deals consummated in the FX Forwards market. Forward points represent the interest rate differential between the two currencies traded and are quoted as a premium or a discount. Forward points are added to, or subtracted from, the spot rate to create the rate of the forward trade.")
  """
  An optional element used for deals consummated in the FX Forwards market. Forward points represent the interest rate differential between the two currencies traded and are quoted as a premium or a discount. Forward points are added to, or subtracted from, the spot rate to create the rate of the forward trade.
  """
  rate: Decimal = Field(..., description="The exchange rate used to cross between the traded currencies.")
  """
  The exchange rate used to cross between the traded currencies.
  """
  spotRate: Optional[Decimal] = Field(None, description="An optional element used for FX forwards and certain types of FX OTC options. For deals consummated in the FX Forwards Market, this represents the current market rate for a particular currency pair.")
  """
  An optional element used for FX forwards and certain types of FX OTC options. For deals consummated in the FX Forwards Market, this represents the current market rate for a particular currency pair.
  """
  
  @rosetta_condition
  def condition_0_CrossRate(self):
    def _then_fn0():
      return ((self.spotRate) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.forwardPoints) is not None), _then_fn0, _else_fn0)


CrossRate.update_forward_refs()
