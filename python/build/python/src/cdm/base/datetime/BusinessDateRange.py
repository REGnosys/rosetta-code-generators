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

__all__ = ['BusinessDateRange']

from cdm.base.datetime.DateRange import DateRange

class BusinessDateRange(DateRange):
  """
  A class defining a range of contiguous business days by defining an unadjusted first date, an unadjusted last date and a business day convention and business centers for adjusting the first and last dates if they would otherwise fall on a non business day in the specified business centers. The days between the first and last date must also be good business days in the specified centers to be counted in the range.
  """
  businessCenters: Optional[BusinessCenters] = Field(None, description="The business center(s), specified either explicitly or by reference to those specified somewhere else in the instance document.")
  """
  The business center(s), specified either explicitly or by reference to those specified somewhere else in the instance document.
  """
  businessDayConvention: BusinessDayConventionEnum = Field(..., description="The convention for adjusting a date if it would otherwise fall on a day that is not a business day, as specified by an ISDA convention (e.g. Following, Precedent).")
  """
  The convention for adjusting a date if it would otherwise fall on a day that is not a business day, as specified by an ISDA convention (e.g. Following, Precedent).
  """

from cdm.base.datetime.BusinessCenters import BusinessCenters
from cdm.base.datetime.BusinessDayConventionEnum import BusinessDayConventionEnum

BusinessDateRange.update_forward_refs()
