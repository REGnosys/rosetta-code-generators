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

__all__ = ['QuasiGovernmentIssuerType']


class QuasiGovernmentIssuerType(BaseDataClass):
  """
  Represents a class to allow specification of different types of Quasi Government collateral.
  """
  sovereignEntity: bool = Field(..., description="True if sovereign entity (e.g. not separate legal personality from sovereign) or false if non-sovereign entity (e.g. separate legal personality from sovereign).")
  """
  True if sovereign entity (e.g. not separate legal personality from sovereign) or false if non-sovereign entity (e.g. separate legal personality from sovereign).
  """
  sovereignRecourse: Optional[bool] = Field(None, description="Applies to non-sovereign entity (e.g. separate legal personality from sovereign).  True if entity has recourse to sovereign (e.g. debt guaranteed by government).  False if entity does not have recourse to sovereign.")
  """
  Applies to non-sovereign entity (e.g. separate legal personality from sovereign).  True if entity has recourse to sovereign (e.g. debt guaranteed by government).  False if entity does not have recourse to sovereign.
  """
  
  @rosetta_condition
  def condition_0_NonSovereignEntityRecourse(self):
    def _then_fn0():
      return all_elements(self.sovereignEntity, "=", False)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.sovereignRecourse) is not None), _then_fn0, _else_fn0)


QuasiGovernmentIssuerType.update_forward_refs()
