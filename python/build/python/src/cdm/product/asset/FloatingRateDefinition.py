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

__all__ = ['FloatingRateDefinition']


class FloatingRateDefinition(BaseDataClass):
  """
  A data defining:  parameters associated with a floating rate reset. This data forms:  part of the cashflows representation of a stream.
  """
  calculatedRate: Optional[Decimal] = Field(None, description="The final calculated rate for a calculation period after any required averaging of rates A calculated rate of 5% would be represented as 0.05.")
  """
  The final calculated rate for a calculation period after any required averaging of rates A calculated rate of 5% would be represented as 0.05.
  """
  capRate: List[Strike] = Field([], description="The cap rate, if any, which applies to the floating rate for the calculation period. The cap rate (strike) is only required where the floating rate on a swap stream is capped at a certain strike level. The cap rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. A cap rate of 5% would be represented as 0.05.")
  """
  The cap rate, if any, which applies to the floating rate for the calculation period. The cap rate (strike) is only required where the floating rate on a swap stream is capped at a certain strike level. The cap rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. A cap rate of 5% would be represented as 0.05.
  """
  floatingRateMultiplier: Optional[Decimal] = Field(None, description="A rate multiplier to apply to the floating rate. The multiplier can be a positive or negative decimal. This element should only be included if the multiplier is not equal to 1 (one).")
  """
  A rate multiplier to apply to the floating rate. The multiplier can be a positive or negative decimal. This element should only be included if the multiplier is not equal to 1 (one).
  """
  floorRate: List[Strike] = Field([], description="The floor rate, if any, which applies to the floating rate for the calculation period. The floor rate (strike) is only required where the floating rate on a swap stream is floored at a certain strike level. The floor rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. The floor rate of 5% would be represented as 0.05.")
  """
  The floor rate, if any, which applies to the floating rate for the calculation period. The floor rate (strike) is only required where the floating rate on a swap stream is floored at a certain strike level. The floor rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. The floor rate of 5% would be represented as 0.05.
  """
  rateObservation: List[RateObservation] = Field([], description="The details of a particular rate observation, including the fixing date and observed rate. A list of rate observation elements may be ordered in the document by ascending adjusted fixing date. An FpML document containing an unordered list of rate observations is still regarded as a conformant document.")
  """
  The details of a particular rate observation, including the fixing date and observed rate. A list of rate observation elements may be ordered in the document by ascending adjusted fixing date. An FpML document containing an unordered list of rate observations is still regarded as a conformant document.
  """
  spread: Optional[Decimal] = Field(None, description="The ISDA Spread, if any, which applies for the calculation period. The spread is a per annum rate, expressed as a decimal. For purposes of determining a calculation period amount, if positive the spread will be added to the floating rate and if negative the spread will be subtracted from the floating rate. A positive 10 basis point (0.1%) spread would be represented as 0.001.")
  """
  The ISDA Spread, if any, which applies for the calculation period. The spread is a per annum rate, expressed as a decimal. For purposes of determining a calculation period amount, if positive the spread will be added to the floating rate and if negative the spread will be subtracted from the floating rate. A positive 10 basis point (0.1%) spread would be represented as 0.001.
  """
  
  @rosetta_condition
  def condition_0_FloatingRateMultiplier(self):
    """
    FpML specifies that the floatingRateMultiplier should only be included if different from 1.
    """
    def _then_fn0():
      return any_elements(self.floatingRateMultiplier, "<>", 1)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.floatingRateMultiplier) is not None), _then_fn0, _else_fn0)

from cdm.product.template.Strike import Strike
from cdm.observable.asset.RateObservation import RateObservation

FloatingRateDefinition.update_forward_refs()
