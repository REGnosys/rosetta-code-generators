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

__all__ = ['AdjustableOrRelativeDate']


class AdjustableOrRelativeDate(BaseDataClass):
  """
  A class giving the choice between defining a date as an explicit date together with applicable adjustments or as relative to some other (anchor) date.
  """
  adjustableDate: Optional[AdjustableDate] = Field(None, description="A date that shall be subject to adjustment if it would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date.")
  """
  A date that shall be subject to adjustment if it would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date.
  """
  relativeDate: Optional[AdjustedRelativeDateOffset] = Field(None, description="A date specified as some offset to another date (the anchor date).")
  """
  A date specified as some offset to another date (the anchor date).
  """
  
  @rosetta_condition
  def condition_0_AdjustableOrRelativeDateChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('adjustableDate', 'relativeDate', necessity=True)

from cdm.base.datetime.AdjustableDate import AdjustableDate
from cdm.base.datetime.AdjustedRelativeDateOffset import AdjustedRelativeDateOffset

AdjustableOrRelativeDate.update_forward_refs()
