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

__all__ = ['FxHaircutCurrency']


class FxHaircutCurrency(BaseDataClass):
  """
  A class to specify the reference currency for the purpose of specifying the FX Haircut relating to a posting obligation, as being either the Termination Currency or an FX Designated Currency.
  """
  fxDesignatedCurrency: Optional[AttributeWithMeta[str] | str] = Field(None, description="When specified, the reference currency for the purpose of specifying the FX Haircut relating to a posting obligation. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
  """
  When specified, the reference currency for the purpose of specifying the FX Haircut relating to a posting obligation. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.
  """
  isTerminationCurrency: bool = Field(..., description="The reference currency for the purpose of specifying the FX Haircut relating to a posting obligation is the Termination Currency when the Boolean value is set to True.")
  """
  The reference currency for the purpose of specifying the FX Haircut relating to a posting obligation is the Termination Currency when the Boolean value is set to True.
  """
  
  @rosetta_condition
  def condition_0_TerminationCurrency(self):
    """
    The FX Designated Currency shouldn't be specified when the reference currency for the purpose of specifying the FX Haircut relating to a posting obligation is specified as the Termination Currency.
    """
    def _then_fn0():
      return ((self.fxDesignatedCurrency) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isTerminationCurrency, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_FxDesignatedCurrency(self):
    """
    The FX Designated Currency should be specified when the reference currency for the purpose of specifying the FX Haircut relating to a posting obligation is specified as not being the Termination Currency.
    """
    def _then_fn0():
      return ((self.fxDesignatedCurrency) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isTerminationCurrency, "=", False), _then_fn0, _else_fn0)


FxHaircutCurrency.update_forward_refs()
