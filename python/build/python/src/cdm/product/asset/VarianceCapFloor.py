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

__all__ = ['VarianceCapFloor']


class VarianceCapFloor(BaseDataClass):
  boundedVariance: Optional[BoundedVariance] = Field(None, description="Conditions which bound variance. The contract specifies one or more boundary levels. These levels are expressed as prices for confirmation purposes Underlyer price must be equal to or higher than Lower Barrier is known as Up Conditional Swap Underlyer price must be equal to or lower than Upper Barrier is known as Down Conditional Swap Underlyer price must be equal to or higher than Lower Barrier and must be equal to or lower than Upper Barrier is known as Barrier Conditional Swap.")
  """
  Conditions which bound variance. The contract specifies one or more boundary levels. These levels are expressed as prices for confirmation purposes Underlyer price must be equal to or higher than Lower Barrier is known as Up Conditional Swap Underlyer price must be equal to or lower than Upper Barrier is known as Down Conditional Swap Underlyer price must be equal to or higher than Lower Barrier and must be equal to or lower than Upper Barrier is known as Barrier Conditional Swap.
  """
  unadjustedVarianceCap: Optional[Decimal] = Field(None, description="For use when varianceCap is applicable. Contains the scaling factor of the Variance Cap that can differ on a trade-by-trade basis in the European market. For example, a Variance Cap of 2.5^2 x Variance Strike Price has an unadjustedVarianceCap of 2.5.")
  """
  For use when varianceCap is applicable. Contains the scaling factor of the Variance Cap that can differ on a trade-by-trade basis in the European market. For example, a Variance Cap of 2.5^2 x Variance Strike Price has an unadjustedVarianceCap of 2.5.
  """
  varianceCap: bool = Field(..., description="If present and true, then variance cap is applicable.")
  """
  If present and true, then variance cap is applicable.
  """
  
  @rosetta_condition
  def condition_0_PositiveUnadjustedVarianceCap(self):
    """
    Unadjusted variance cap must be positive
    """
    def _then_fn0():
      return all_elements(self.unadjustedVarianceCap, ">", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.unadjustedVarianceCap) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_CapFloorApplicability(self):
    """
    Caps/floors can and must be specified if varianceCap is set to true. If false, barriers cannot be established
    """
    def _then_fn0():
      return (((self.unadjustedVarianceCap) is not None) or ((self.boundedVariance) is not None))
    
    def _else_fn0():
      return (((self.unadjustedVarianceCap) is None) and ((self.boundedVariance) is None))
    
    return if_cond_fn(all_elements(self.varianceCap, "=", False), _then_fn0, _else_fn0)

from cdm.product.asset.BoundedVariance import BoundedVariance

VarianceCapFloor.update_forward_refs()
