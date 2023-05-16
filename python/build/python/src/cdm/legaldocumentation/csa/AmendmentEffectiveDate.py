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

__all__ = ['AmendmentEffectiveDate']


class AmendmentEffectiveDate(BaseDataClass):
  """
  A class to specify the effective date of the Amendment to Termination Currency. This date can be specified as either an actual date, a specific date (e.g. the annex date) or as a custom provision. 
  """
  customProvision: Optional[str] = Field(None, description="The effective date of the Amendment to Termination Currency when specified as a non normalized custom provision.")
  """
  The effective date of the Amendment to Termination Currency when specified as a non normalized custom provision.
  """
  date: Optional[date] = Field(None, description="The effective date of the Amendment to Termination Currency when specified as an actual date.")
  """
  The effective date of the Amendment to Termination Currency when specified as an actual date.
  """
  specificDate: Optional[AmendmentEffectiveDateEnum] = Field(None, description="The effective date of the Amendment to Termination Currency when specified as relative to another date (e.g. the annex date).")
  """
  The effective date of the Amendment to Termination Currency when specified as relative to another date (e.g. the annex date).
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('date', 'specificDate', 'customProvision', necessity=True)

from cdm.legaldocumentation.csa.AmendmentEffectiveDateEnum import AmendmentEffectiveDateEnum

AmendmentEffectiveDate.update_forward_refs()
