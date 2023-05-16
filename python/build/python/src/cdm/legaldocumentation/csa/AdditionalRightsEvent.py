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

__all__ = ['AdditionalRightsEvent']


class AdditionalRightsEvent(BaseDataClass):
  """
  A class to specify the Pledgor/Obligor/Chargor Additional Rights Event election. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (k): Chargor Additional Rights Event. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (k): Obligor Additional Rights Event. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (k): Pledgor Additional Rights Event.
  """
  isApplicable: bool = Field(..., description="The Pledgor Additional Rights Event election is applicable when True, and not applicable when False.")
  """
  The Pledgor Additional Rights Event election is applicable when True, and not applicable when False.
  """
  qualification: Optional[str] = Field(None, description="The qualification of the Pledgor Additional Rights Event election, when specified.")
  """
  The qualification of the Pledgor Additional Rights Event election, when specified.
  """
  
  @rosetta_condition
  def condition_0_Qualification(self):
    """
    The Pledgor/Obligor/Chargor Additional Rights should be qualified only when the Pledgor Additional Rights Event election is specified as applicable.
    """
    def _then_fn0():
      return all_elements(self.isApplicable, "=", False)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.qualification) is not None), _then_fn0, _else_fn0)


AdditionalRightsEvent.update_forward_refs()
