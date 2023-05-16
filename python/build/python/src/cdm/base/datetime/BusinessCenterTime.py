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

__all__ = ['BusinessCenterTime']


class BusinessCenterTime(BaseDataClass):
  """
  A class for defining a time with respect to a business day calendar location. For example, 11:00:00 GBLO.
  """
  businessCenter: AttributeWithMeta[BusinessCenterEnum] | BusinessCenterEnum = Field(..., description="A code identifying a business day calendar location. A business day calendar location is drawn from the list identified by the business day calendar location enumeration.")
  """
  A code identifying a business day calendar location. A business day calendar location is drawn from the list identified by the business day calendar location enumeration.
  """
  hourMinuteTime: time = Field(..., description="A time specified in hh:mm:ss format where the second component must be '00', e.g. 11am would be represented as 11:00:00.")
  """
  A time specified in hh:mm:ss format where the second component must be '00', e.g. 11am would be represented as 11:00:00.
  """

from cdm.base.datetime.BusinessCenterEnum import BusinessCenterEnum

BusinessCenterTime.update_forward_refs()
