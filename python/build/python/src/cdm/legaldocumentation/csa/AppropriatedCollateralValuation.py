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

__all__ = ['AppropriatedCollateralValuation']


class AppropriatedCollateralValuation(BaseDataClass):
  """
  A class to specify the Valuation of Appropriated Collateral that is applicable to the English Law ISDA CSA. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (u): Valuation of Appropriated Collateral.
  """
  election: Optional[str] = Field(None, description="The parties' election that qualify the Valuation of Appropriate Collateral in the case where it is deemed applicable.")
  """
  The parties' election that qualify the Valuation of Appropriate Collateral in the case where it is deemed applicable.
  """
  isSpecified: bool = Field(..., description="The qualification of whether the Valuation of Appropriate Collateral provision is applicable (True) or not applicable (False).")
  """
  The qualification of whether the Valuation of Appropriate Collateral provision is applicable (True) or not applicable (False).
  """
  
  @rosetta_condition
  def condition_0_Specified(self):
    """
    The Valuation of Appropriate Collateral election must be specified when it is applicable.
    """
    def _then_fn0():
      return ((self.election) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isSpecified, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_NotSpecified(self):
    """
    The Valuation of Appropriate Collateral election cannot be specified when it is not applicable.
    """
    def _then_fn0():
      return ((self.election) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isSpecified, "=", False), _then_fn0, _else_fn0)


AppropriatedCollateralValuation.update_forward_refs()
