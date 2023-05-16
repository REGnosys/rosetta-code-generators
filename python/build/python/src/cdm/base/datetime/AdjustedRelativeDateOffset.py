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

__all__ = ['AdjustedRelativeDateOffset']

from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset

class AdjustedRelativeDateOffset(RelativeDateOffset):
  """
  A type defining a date (referred to as the derived date) as a relative offset from another date (referred to as the anchor date) plus optional date adjustments.
  """
  relativeDateAdjustments: Optional[BusinessDayAdjustments] = Field(None, description="The business day convention and financial business centers used for adjusting the relative date if it would otherwise fall on a day that is not a business date in the specified business centers.")
  """
  The business day convention and financial business centers used for adjusting the relative date if it would otherwise fall on a day that is not a business date in the specified business centers.
  """

from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments

AdjustedRelativeDateOffset.update_forward_refs()
