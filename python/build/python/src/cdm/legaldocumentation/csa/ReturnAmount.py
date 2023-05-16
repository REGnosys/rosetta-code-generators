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

__all__ = ['ReturnAmount']


class ReturnAmount(BaseDataClass):
  """
  A class to specify the application of Interest Amount with respect the Return Amount. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).
  """
  customElection: Optional[str] = Field(None, description="Custom election that might be specified by the parties to the agreement.")
  """
  Custom election that might be specified by the parties to the agreement.
  """
  includesDefaultLanguage: Optional[bool] = Field(None, description="Default language is included when True, and excluded when False.")
  """
  Default language is included when True, and excluded when False.
  """
  
  @rosetta_condition
  def condition_0_CustomElection(self):
    """
    A data rule to specify that when a custom election exists then default language should not be included.
    """
    def _then_fn0():
      return all_elements(self.includesDefaultLanguage, "=", False)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.customElection) is not None), _then_fn0, _else_fn0)


ReturnAmount.update_forward_refs()
