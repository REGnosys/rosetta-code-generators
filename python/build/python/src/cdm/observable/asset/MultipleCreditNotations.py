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

__all__ = ['MultipleCreditNotations']


class MultipleCreditNotations(BaseDataClass):
  """
  Represetns a class to specify multiple credit notations alongside a conditional 'any' or 'all' qualifier.
  """
  condition: QuantifierEnum = Field(..., description="An enumerated element, to qualify whether All or Any credit notation applies.")
  """
  An enumerated element, to qualify whether All or Any credit notation applies.
  """
  creditNotation: List[AttributeWithMeta[CreditNotation] | CreditNotation] = Field([], description="At least two credit notations much be specified.")
  """
  At least two credit notations much be specified.
  """
  @rosetta_condition
  def cardinality_creditNotation(self):
    return check_cardinality(self.creditNotation, 2, None)
  
  mismatchResolution: Optional[CreditNotationMismatchResolutionEnum] = Field(None, description="")
  referenceAgency: Optional[CreditRatingAgencyEnum] = Field(None, description="")
  
  @rosetta_condition
  def condition_0_ReferenceAgency(self):
    """
    If the mismatch resolution is ReferenceAgency, ensure that the reference agency is specified.
    """
    def _then_fn0():
      return ((MultipleCreditNotations.referenceAgency) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(MultipleCreditNotations.mismatchResolution, "=", CreditNotationMismatchResolutionEnum.REFERENCE_AGENCY), _then_fn0, _else_fn0)

from cdm.base.math.QuantifierEnum import QuantifierEnum
from cdm.observable.asset.CreditNotation import CreditNotation
from cdm.observable.asset.CreditNotationMismatchResolutionEnum import CreditNotationMismatchResolutionEnum
from cdm.observable.asset.CreditRatingAgencyEnum import CreditRatingAgencyEnum

MultipleCreditNotations.update_forward_refs()
