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

__all__ = ['AdjustableOrAdjustedOrRelativeDate']


class AdjustableOrAdjustedOrRelativeDate(BaseDataClass):
  """
  This Rosetta class specifies the date as either an unadjusted, adjusted or relative date. It supplements the features of the AdjustableOrAdjustedDate to support the credit default swap option premium, which uses the relative date construct.
  """
  adjustedDate: Optional[AttributeWithMeta[date] | date] = Field(None, description="The date once the adjustment has been performed. (Note that this date may change if the business center holidays change).")
  """
  The date once the adjustment has been performed. (Note that this date may change if the business center holidays change).
  """
  dateAdjustments: Optional[BusinessDayAdjustments] = Field(None, description="The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.")
  """
  The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.
  """
  relativeDate: Optional[RelativeDateOffset] = Field(None, description="A date specified as some offset to another date (the anchor date).")
  """
  A date specified as some offset to another date (the anchor date).
  """
  unadjustedDate: Optional[date] = Field(None, description="A date subject to adjustment.")
  """
  A date subject to adjustment.
  """
  
  @rosetta_condition
  def condition_0_AdjustedDate(self):
    """
    This data rule extends the data rule AdjustableOrAdjustedDate_adjustedDate by specifying logic applicable to the relative date.
    """
    return (((((self.adjustedDate) is not None) or ((self.relativeDate) is not None)) or ((self.unadjustedDate) is not None)) or ((((self.unadjustedDate) is not None) and ((self.dateAdjustments) is not None)) and ((self.adjustedDate) is None)))

from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments
from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset

AdjustableOrAdjustedOrRelativeDate.update_forward_refs()
