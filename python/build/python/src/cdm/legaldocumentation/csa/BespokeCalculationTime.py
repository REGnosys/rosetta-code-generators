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

__all__ = ['BespokeCalculationTime']


class BespokeCalculationTime(BaseDataClass):
  """
  A class to specify additional Calculation Time terms for the purposes of Initial Margin
  """
  asCalculationAgent: bool = Field(..., description="If set to True, the Calculation Time for Initial Margin is the time as of which the Calculation Agent (IM) computes its end of day valuations of derivatives transactions")
  """
  If set to True, the Calculation Time for Initial Margin is the time as of which the Calculation Agent (IM) computes its end of day valuations of derivatives transactions
  """
  bespokeCalculationTimeTerms: Optional[str] = Field(None, description="Additional Terms applicable to Calculation Time for Initial Margin")
  """
  Additional Terms applicable to Calculation Time for Initial Margin
  """
  
  @rosetta_condition
  def condition_0_AsCalculationAgentIm(self):
    """
    A data rule to enforce that the terms applicable to Calculation Time for Initial Margin should be specified when the computation time is not as per Calculation Agent
    """
    def _then_fn0():
      return ((self.bespokeCalculationTimeTerms) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.asCalculationAgent, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_BespokeCalculationTimeTerms(self):
    """
    A data rule to enforce that the Calculation Time for Initial Margin shouldn't be specified when the Control Agreement isn't deemed a Credit Support Document with respect to the party(ies).
    """
    def _then_fn0():
      return ((self.bespokeCalculationTimeTerms) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.asCalculationAgent, "=", False), _then_fn0, _else_fn0)


BespokeCalculationTime.update_forward_refs()
