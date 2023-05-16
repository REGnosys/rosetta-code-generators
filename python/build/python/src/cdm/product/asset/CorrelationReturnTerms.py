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

__all__ = ['CorrelationReturnTerms']

from cdm.product.asset.ReturnTermsBase import ReturnTermsBase

class CorrelationReturnTerms(ReturnTermsBase):
  boundedCorrelation: Optional[NumberRange] = Field(None, description="Describes correlation bounds, which form a cap and a floor on the realized correlation.")
  """
  Describes correlation bounds, which form a cap and a floor on the realized correlation.
  """
  correlationStrikePrice: Price = Field(..., description="Correlation Strike Price in accordance with the ISDA 2011 Equity Derivatives Definitions.")
  """
  Correlation Strike Price in accordance with the ISDA 2011 Equity Derivatives Definitions.
  """
  numberOfDataSeries: Optional[int] = Field(None, description="Number of data series, normal market practice is that correlation data sets are drawn from geographic market areas, such as America, Europe and Asia Pacific, each of these geographic areas will have its own data series to avoid contagion.")
  """
  Number of data series, normal market practice is that correlation data sets are drawn from geographic market areas, such as America, Europe and Asia Pacific, each of these geographic areas will have its own data series to avoid contagion.
  """
  
  @rosetta_condition
  def condition_0_PositiveNumberOfDataSeries(self):
    """
    The number of data series must be positive
    """
    def _then_fn0():
      return all_elements(self.numberOfDataSeries, ">", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.numberOfDataSeries) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_CorrelationValue(self):
    """
    The correlation strike price is a decimal with allowed values only between 1 and -1
    """
    return (all_elements(self.correlationStrikePrice.value, ">", -1) and all_elements(self.correlationStrikePrice.value, ">", 1))

from cdm.base.math.NumberRange import NumberRange
from cdm.observable.asset.Price import Price

CorrelationReturnTerms.update_forward_refs()
