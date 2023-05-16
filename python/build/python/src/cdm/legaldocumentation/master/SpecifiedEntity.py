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

__all__ = ['SpecifiedEntity']


class SpecifiedEntity(BaseDataClass):
  """
  Description
  """
  materialSubsidiaryTerms: Optional[str] = Field(None, description="The meaning of Material Subsidiary for the Event of Default or Termination Event specified.")
  """
  The meaning of Material Subsidiary for the Event of Default or Termination Event specified.
  """
  otherSpecifiedEntityTerms: Optional[str] = Field(None, description="The non standard terms for the Event of Default or Termination Event specified.")
  """
  The non standard terms for the Event of Default or Termination Event specified.
  """
  party: Party = Field(..., description="The elective party")
  """
  The elective party
  """
  specifiedEntity: List[LegalEntity] = Field([], description="The specified entities for the Event of Default or Termination Event specified.")
  """
  The specified entities for the Event of Default or Termination Event specified.
  """
  specifiedEntityTerms: SpecifiedEntityTermsEnum = Field(..., description="The specified entity terms for the Event of Default or Termination Event specified.")
  """
  The specified entity terms for the Event of Default or Termination Event specified.
  """
  
  @rosetta_condition
  def condition_0_SpecifiedEntity(self):
    """
    A validation rule to ensure that a SpecifiedEntity is specified when required.
    """
    def _then_fn0():
      return ((self.specifiedEntity) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.specifiedEntityTerms, "=", SpecifiedEntityTermsEnum.NAMED_SPECIFIED_ENTITY), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_MaterialSubsidiary(self):
    """
    A validation rule to ensure that Material Subsidiary terms are specified when required.
    """
    def _then_fn0():
      return ((self.materialSubsidiaryTerms) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.specifiedEntityTerms, "=", SpecifiedEntityTermsEnum.MATERIAL_SUBSIDIARY), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_OtherSpecifiedEntity(self):
    """
    A validation rule to ensure that non standard Specified Entity terms are provided when required.
    """
    def _then_fn0():
      return ((self.otherSpecifiedEntityTerms) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.specifiedEntityTerms, "=", SpecifiedEntityTermsEnum.OTHER_SPECIFIED_ENTITY), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.LegalEntity import LegalEntity
from cdm.legaldocumentation.common.SpecifiedEntityTermsEnum import SpecifiedEntityTermsEnum

SpecifiedEntity.update_forward_refs()
