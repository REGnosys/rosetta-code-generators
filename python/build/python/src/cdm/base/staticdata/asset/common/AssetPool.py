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

__all__ = ['AssetPool']


class AssetPool(BaseDataClass):
  """
  Characterizes the asset pool behind an asset backed bond.
  """
  currentFactor: Optional[Decimal] = Field(None, description="The part of the mortgage that is currently outstanding. It is expressed similarly to the initial factor, as factor multiplier to the mortgage. This term is formally defined as part of the 'ISDA Standard Terms Supplement for use with credit derivatives transactions on mortgage-backed security with pas-as-you-go or physical settlement'.")
  """
  The part of the mortgage that is currently outstanding. It is expressed similarly to the initial factor, as factor multiplier to the mortgage. This term is formally defined as part of the 'ISDA Standard Terms Supplement for use with credit derivatives transactions on mortgage-backed security with pas-as-you-go or physical settlement'.
  """
  effectiveDate: Optional[date] = Field(None, description="Optionally it is possible to specify a version effective date when a version is supplied.")
  """
  Optionally it is possible to specify a version effective date when a version is supplied.
  """
  initialFactor: Decimal = Field(..., description="The part of the mortgage that is outstanding on trade inception, i.e. has not been repaid yet as principal. It is expressed as a multiplier factor to the mortgage: 1 means that the whole mortgage amount is outstanding, 0.8 means that 20% has been repaid.")
  """
  The part of the mortgage that is outstanding on trade inception, i.e. has not been repaid yet as principal. It is expressed as a multiplier factor to the mortgage: 1 means that the whole mortgage amount is outstanding, 0.8 means that 20% has been repaid.
  """
  version: Optional[str] = Field(None, description="The asset pool version.")
  """
  The asset pool version.
  """
  
  @rosetta_condition
  def condition_0_EffectiveDate(self):
    """
    FpML specifies that it is possible to specify a version effective date when a versionId is supplied.
    """
    def _then_fn0():
      return ((self.effectiveDate) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.version) is None), _then_fn0, _else_fn0)


AssetPool.update_forward_refs()
