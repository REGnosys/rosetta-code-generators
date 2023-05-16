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

__all__ = ['AdditionalRepresentations']


class AdditionalRepresentations(BaseDataClass):
  """
  A class to specify Additional Representations that may be applicable to an agreement.
  """
  additionalRepresentation: Optional[AdditionalRepresentation] = Field(None, description="The specification of the Additional Representation that may be applicable to the agreement.")
  """
  The specification of the Additional Representation that may be applicable to the agreement.
  """
  regulatoryComplianceRepresentation: Optional[bool] = Field(None, description="The qualification of whether Additional Information related to Regulatory Compliance and Concentration Limits is applicable or not.")
  """
  The qualification of whether Additional Information related to Regulatory Compliance and Concentration Limits is applicable or not.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('additionalRepresentation', 'regulatoryComplianceRepresentation', necessity=True)

from cdm.legaldocumentation.csa.AdditionalRepresentation import AdditionalRepresentation

AdditionalRepresentations.update_forward_refs()
