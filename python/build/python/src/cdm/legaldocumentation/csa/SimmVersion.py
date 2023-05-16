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

__all__ = ['SimmVersion']


class SimmVersion(BaseDataClass):
  """
  A class to specify the ISDA SIMM version that applies to the ISDA 2018 CSA for Initial Margin. According to the ISDA 2018 CSA for Initial Margin, Paragraph 13, General Principles (ee) (1) provisions, the SIMM version is either not specified, or references a version used by one of the parties to the agreement.
  """
  asSpecified: Optional[str] = Field(None, description="The SIMM version exception when specified as a customized approach by the party.")
  """
  The SIMM version exception when specified as a customized approach by the party.
  """
  isSpecified: Optional[bool] = Field(None, description="A boolean attribute to determine whether the SIMM version is specified for the purpose of the legal agreement.")
  """
  A boolean attribute to determine whether the SIMM version is specified for the purpose of the legal agreement.
  """
  partyVersion: Optional[CounterpartyRoleEnum] = Field(None, description="The party which the specified SIMM version applies to.")
  """
  The party which the specified SIMM version applies to.
  """
  
  @rosetta_condition
  def condition_0_VersionNotSpecified(self):
    """
    A data rule to enforce that the version attribute should be absent when the SIMM version is stated as not specified for the CSA.
    """
    def _then_fn0():
      return ((self.partyVersion) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isSpecified, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_VersionSpecified(self):
    """
    A data rule to enforce that the version attribute should be specified when the SIMM version is stated as specified for the CSA.
    """
    def _then_fn0():
      return ((self.partyVersion) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isSpecified, "=", False), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

SimmVersion.update_forward_refs()
