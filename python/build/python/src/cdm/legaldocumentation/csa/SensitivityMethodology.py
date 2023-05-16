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

__all__ = ['SensitivityMethodology']


class SensitivityMethodology(BaseDataClass):
  """
  A class to specify the methodology according to which sensitivities to (i) equity indices, funds and ETFs, and (ii) commodity indices are computed. This specification is done either through a normalized election as part of the specifiedMethodology, or through a custom election via the customMethodology attribute. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (gg)(2).
  """
  customMethodology: Optional[str] = Field(None, description="The methodology according to which sensitivities will be computed, when specified through a custom election.")
  """
  The methodology according to which sensitivities will be computed, when specified through a custom election.
  """
  specifiedMethodology: Optional[SensitivitiesEnum] = Field(None, description="The methodology according to which sensitivities will be computed, when specified through a normalized election.")
  """
  The methodology according to which sensitivities will be computed, when specified through a normalized election.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('specifiedMethodology', 'customMethodology', necessity=True)

from cdm.legaldocumentation.csa.SensitivitiesEnum import SensitivitiesEnum

SensitivityMethodology.update_forward_refs()
