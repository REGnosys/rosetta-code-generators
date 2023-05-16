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

__all__ = ['AdjustableDates']


class AdjustableDates(BaseDataClass):
  """
  A class for defining a series of dates that shall be subject to adjustment if they would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the dates.
  """
  adjustedDate: List[AttributeWithMeta[date] | date] = Field([], description="The date(s) once the adjustment has been performed. (Note that this date may change if the business center holidays change).")
  """
  The date(s) once the adjustment has been performed. (Note that this date may change if the business center holidays change).
  """
  dateAdjustments: Optional[BusinessDayAdjustments] = Field(None, description="The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.")
  """
  The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.
  """
  unadjustedDate: List[date] = Field([], description="A date subject to adjustment.")
  """
  A date subject to adjustment.
  """
  
  @rosetta_condition
  def condition_0_AdjustedDate(self):
    """
    FpML specifies a choice between adjustedDate and [unadjustedDate (required), dateAdjutsments (required), adjustedDate (optional)].
    """
    def _then_fn0():
      return (((self.unadjustedDate) is not None) and ((self.dateAdjustments) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.adjustedDate) is None), _then_fn0, _else_fn0)

from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments

AdjustableDates.update_forward_refs()
