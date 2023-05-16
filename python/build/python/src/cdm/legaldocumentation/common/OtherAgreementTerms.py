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

__all__ = ['OtherAgreementTerms']


class OtherAgreementTerms(BaseDataClass):
  """
  A class to specify a related legal agreement. For example, ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (s): Other CSA and Japanese Law CSA (VM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (o): Other CSA.
  """
  isSpecified: bool = Field(..., description="The qualification of whether some other related agreement is specified (True) or not (False).")
  """
  The qualification of whether some other related agreement is specified (True) or not (False).
  """
  legalDocument: Optional[str] = Field(None, description="The specification of this other agreement, when the qualification is True.")
  """
  The specification of this other agreement, when the qualification is True.
  """
  
  @rosetta_condition
  def condition_0_LegalDocumentNotSpecified(self):
    """
    A data rule to enforce that the related legal agreement should not be referenced if it is deemed as not specified as part of the boolean attribute.
    """
    def _then_fn0():
      return ((self.legalDocument) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isSpecified, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_LegalDocumentSpecified(self):
    """
    A data rule to enforce that the related legal agreement should be referenced if it is deemed as specified as part of the boolean attribute.
    """
    def _then_fn0():
      return ((self.legalDocument) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isSpecified, "=", False), _then_fn0, _else_fn0)


OtherAgreementTerms.update_forward_refs()
