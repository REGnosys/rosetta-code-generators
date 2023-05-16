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

__all__ = ['AgencyRatingCriteria']


class AgencyRatingCriteria(BaseDataClass):
  """
  Represents a class to specify multiple credit notations alongside a conditional 'any' or 'all' qualifier.
  """
  boundary: Optional[CreditNotationBoundaryEnum] = Field(None, description="Indicates the boundary of a credit agency rating i.e minimum or maximum.")
  """
  Indicates the boundary of a credit agency rating i.e minimum or maximum.
  """
  creditNotation: List[CreditNotation] = Field([], description="Indicates the agency rating criteria specified for the asset or issuer.")
  """
  Indicates the agency rating criteria specified for the asset or issuer.
  """
  @rosetta_condition
  def cardinality_creditNotation(self):
    return check_cardinality(self.creditNotation, 1, None)
  
  mismatchResolution: Optional[CreditNotationMismatchResolutionEnum] = Field(None, description="Indicator for options to be used if several agency ratings (>1) are specified and its necessary to identify specific charateristics. i.e (lowest or highest).")
  """
  Indicator for options to be used if several agency ratings (>1) are specified and its necessary to identify specific charateristics. i.e (lowest or highest).
  """
  qualifier: QuantifierEnum = Field(..., description="Indicates whether all or any agency ratings apply.")
  """
  Indicates whether all or any agency ratings apply.
  """
  referenceAgency: Optional[CreditRatingAgencyEnum] = Field(None, description="identifies the dominant reference agency if there is a missmatch and several reference agencies exsist.")
  """
  identifies the dominant reference agency if there is a missmatch and several reference agencies exsist.
  """
  
  @rosetta_condition
  def condition_0_ReferenceAgency(self):
    """
    If the mismatch resolution is ReferenceAgency, ensure that the reference agency is specified.
    """
    def _then_fn0():
      return ((AgencyRatingCriteria.referenceAgency) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(AgencyRatingCriteria.mismatchResolution, "=", CreditNotationMismatchResolutionEnum.REFERENCE_AGENCY), _then_fn0, _else_fn0)

from cdm.observable.asset.CreditNotationBoundaryEnum import CreditNotationBoundaryEnum
from cdm.observable.asset.CreditNotation import CreditNotation
from cdm.observable.asset.CreditNotationMismatchResolutionEnum import CreditNotationMismatchResolutionEnum
from cdm.base.math.QuantifierEnum import QuantifierEnum
from cdm.observable.asset.CreditRatingAgencyEnum import CreditRatingAgencyEnum

AgencyRatingCriteria.update_forward_refs()
