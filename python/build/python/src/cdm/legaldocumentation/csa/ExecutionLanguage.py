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

__all__ = ['ExecutionLanguage']


class ExecutionLanguage(BaseDataClass):
  """
  A class to specify execution language terms of a Security Agreement.
  """
  numberOfOriginals: Optional[str] = Field(None, description="The number of original documents")
  """
  The number of original documents
  """
  otherLanguage: Optional[str] = Field(None, description="Bespoke execution language to be included when specified.")
  """
  Bespoke execution language to be included when specified.
  """
  standardLanguage: bool = Field(..., description="A boolean attribute to determine if standard language is applicable or not")
  """
  A boolean attribute to determine if standard language is applicable or not
  """
  
  @rosetta_condition
  def condition_0_NumberOfOriginals(self):
    """
    A data rule to enforce that the number of original documents should only be specified when standard execution language is used.
    """
    def _then_fn0():
      return ((self.numberOfOriginals) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.standardLanguage, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_OtherLanguage(self):
    """
    A data rule to enforce that bespoke execution language must be included if non-standard execution language is specified.
    """
    def _then_fn0():
      return ((self.otherLanguage) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.standardLanguage, "=", False), _then_fn0, _else_fn0)


ExecutionLanguage.update_forward_refs()
