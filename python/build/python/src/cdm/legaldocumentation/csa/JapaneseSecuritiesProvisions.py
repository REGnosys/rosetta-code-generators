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

__all__ = ['JapaneseSecuritiesProvisions']


class JapaneseSecuritiesProvisions(BaseDataClass):
  """
  A class to specify Japanese Securities Provision elections.
  """
  amendmentsToJapaneseProvisions: Optional[bool] = Field(None, description="Additional Amendments to Japanese Securities Provisions are specified when True, and not specified when False")
  """
  Additional Amendments to Japanese Securities Provisions are specified when True, and not specified when False
  """
  amendmentsToJapaneseProvisionsTerms: Optional[str] = Field(None, description="Specific terms applicable to Additional Amendments to Japanese Securities Provisions")
  """
  Specific terms applicable to Additional Amendments to Japanese Securities Provisions
  """
  clearstreamAmendmentToJapaneseProvisions: Optional[bool] = Field(None, description="Specification of whether Clearstream Event amendment language is included (true) or excluded (false).")
  """
  Specification of whether Clearstream Event amendment language is included (true) or excluded (false).
  """
  isApplicable: bool = Field(..., description="Japanese Securities Provisions are applicable when True and Not Applicable when False")
  """
  Japanese Securities Provisions are applicable when True and Not Applicable when False
  """
  relevantProvisionsElection: Optional[bool] = Field(None, description="Recommended Japanese Securities Provisions are applicable when True, additional Provisions are specified when False")
  """
  Recommended Japanese Securities Provisions are applicable when True, additional Provisions are specified when False
  """
  relevantProvisionsTerms: Optional[str] = Field(None, description="Specific terms applicable to Recommended Japanese Securities Provisions")
  """
  Specific terms applicable to Recommended Japanese Securities Provisions
  """
  
  @rosetta_condition
  def condition_0_RelevantProvisionsElection(self):
    """
    A data rule to enforce that the specific terms applicable to Recommended Japanese Securities Provisions should be specified when required
    """
    def _then_fn0():
      return ((self.relevantProvisionsTerms) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.relevantProvisionsElection, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_AmendmentsToJapaneseProvisions(self):
    """
    A data rule to enforce that the specific terms applicable to Additional Amendments to Japanese Securities Provisions should be specified when required
    """
    def _then_fn0():
      return ((self.amendmentsToJapaneseProvisionsTerms) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.amendmentsToJapaneseProvisions, "=", False), _then_fn0, _else_fn0)


JapaneseSecuritiesProvisions.update_forward_refs()
