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

__all__ = ['CollateralAccessBreach']


class CollateralAccessBreach(BaseDataClass):
  """
  A class to specify Collateral Access Breach language
  """
  cabEndDate: Optional[Decimal] = Field(None, description="The business days following the related Collateral Access Breach when the additional terms end ")
  """
  The business days following the related Collateral Access Breach when the additional terms end 
  """
  cabEndDateElection: Optional[bool] = Field(None, description="Determination of whether the Collateral Access Breach end date is a number of days (True) or specified (False)")
  """
  Determination of whether the Collateral Access Breach end date is a number of days (True) or specified (False)
  """
  cabEndDateTerms: Optional[str] = Field(None, description="Specific terms for when Collateral Access Breach terms end")
  """
  Specific terms for when Collateral Access Breach terms end
  """
  isApplicable: bool = Field(..., description="Collateral Access Breach terms are applicable when True and not applicable when False")
  """
  Collateral Access Breach terms are applicable when True and not applicable when False
  """
  
  @rosetta_condition
  def condition_0_CabEndDateTerms(self):
    """
    A condition to require Collateral Access Breach End Date Terms when a specification is required
    """
    def _then_fn0():
      return ((self.cabEndDateTerms) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.cabEndDateElection, "=", False), _then_fn0, _else_fn0)


CollateralAccessBreach.update_forward_refs()
