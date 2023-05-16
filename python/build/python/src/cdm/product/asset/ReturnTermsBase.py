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

__all__ = ['ReturnTermsBase']


class ReturnTermsBase(BaseDataClass):
  """
  Contains all common elements in variance, volatility and correlation return Terms.
  """
  annualizationFactor: Optional[int] = Field(None, description="This specifies the numerator of an annualization factor. Frequently this number is equal to the number of observations of prices in a year e.g. 252.")
  """
  This specifies the numerator of an annualization factor. Frequently this number is equal to the number of observations of prices in a year e.g. 252.
  """
  dividendApplicability: Optional[DividendApplicability] = Field(None, description="The parameters which define whether dividends are applicable")
  """
  The parameters which define whether dividends are applicable
  """
  equityUnderlierProvisions: Optional[EquityUnderlierProvisions] = Field(None, description="Contains Equity Underlyer provisions regarding jurisdiction and fallbacks.")
  """
  Contains Equity Underlyer provisions regarding jurisdiction and fallbacks.
  """
  expectedN: int = Field(..., description="Expected number of trading days.")
  """
  Expected number of trading days.
  """
  initialLevel: Optional[Decimal] = Field(None, description="Contract will strike off this initial level. Providing just the initialLevel without initialLevelSource, infers that this is AgreedInitialPrice - a specified Initial Index Level.")
  """
  Contract will strike off this initial level. Providing just the initialLevel without initialLevelSource, infers that this is AgreedInitialPrice - a specified Initial Index Level.
  """
  initialLevelSource: Optional[DeterminationMethodEnum] = Field(None, description="In this context, this is AgreedInitialPrice - a specified Initial Index Level.")
  """
  In this context, this is AgreedInitialPrice - a specified Initial Index Level.
  """
  meanAdjustment: Optional[bool] = Field(None, description="Specifies whether Mean Adjustment is applicable or not in the calculation of the Realized Volatility, Variance or Correlation")
  """
  Specifies whether Mean Adjustment is applicable or not in the calculation of the Realized Volatility, Variance or Correlation
  """
  performance: Optional[str] = Field(None, description="Performance calculation, in accordance with Part 1 Section 12 of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap, Para 75. 'Equity Performance'. Cumulative performance is used as a notional multiplier factor on both legs of an Equity Swap.")
  """
  Performance calculation, in accordance with Part 1 Section 12 of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap, Para 75. 'Equity Performance'. Cumulative performance is used as a notional multiplier factor on both legs of an Equity Swap.
  """
  sharePriceDividendAdjustment: Optional[bool] = Field(None, description="Indicates whether the price of shares is adjusted for dividends or not.")
  """
  Indicates whether the price of shares is adjusted for dividends or not.
  """
  valuation: Valuation = Field(..., description="Contains all non-date valuation information.")
  """
  Contains all non-date valuation information.
  """
  
  @rosetta_condition
  def condition_0_InitialLevelOrInitialLevelSource(self):
    """
    At least one of initialLevel and initialLevelSource must be present, or both
    """
    def _then_fn1():
      return ((self.initialLevel) is not None)
    
    def _else_fn1():
      return True
    
    def _then_fn0():
      return (((self.initialLevelSource) is not None) and if_cond_fn(((self.initialLevelSource) is None), _then_fn1, _else_fn1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.initialLevel) is None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_PositiveExpectedN(self):
    """
    The number of expected trading dates must be positive
    """
    return all_elements(self.expectedN, ">", 0)

from cdm.observable.asset.DividendApplicability import DividendApplicability
from cdm.product.asset.EquityUnderlierProvisions import EquityUnderlierProvisions
from cdm.observable.common.DeterminationMethodEnum import DeterminationMethodEnum
from cdm.product.asset.Valuation import Valuation

ReturnTermsBase.update_forward_refs()
