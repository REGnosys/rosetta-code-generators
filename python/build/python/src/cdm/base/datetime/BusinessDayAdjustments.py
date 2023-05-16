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

__all__ = ['BusinessDayAdjustments']


class BusinessDayAdjustments(BaseDataClass):
  """
  A class defining the business day convention and financial business centers used for adjusting any relevant date if it would otherwise fall on a day that is not a business day in the specified business center.
  """
  businessCenters: Optional[BusinessCenters] = Field(None, description="The business center(s), specified either explicitly or by reference to those specified somewhere else in the instance document.")
  """
  The business center(s), specified either explicitly or by reference to those specified somewhere else in the instance document.
  """
  businessDayConvention: BusinessDayConventionEnum = Field(..., description="The convention for adjusting a date if it would otherwise fall on a day that is not a business day.")
  """
  The convention for adjusting a date if it would otherwise fall on a day that is not a business day.
  """

from cdm.base.datetime.BusinessCenters import BusinessCenters
from cdm.base.datetime.BusinessDayConventionEnum import BusinessDayConventionEnum

BusinessDayAdjustments.update_forward_refs()
