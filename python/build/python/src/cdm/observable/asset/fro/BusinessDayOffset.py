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

__all__ = ['BusinessDayOffset']

from cdm.base.datetime.Period import Period

class BusinessDayOffset(Period):
  """
  This allows an offset to be specified as, for instance, N business days, with a business centers specified as included.
  """
  businessCenters: Optional[BusinessCenters] = Field(None, description="The business centers for the offset.")
  """
  The business centers for the offset.
  """
  fixingOffsetDefinition: Optional[str] = Field(None, description="Legal text that underlies the Fixing Offset. ISDA Fixing Offset Definition. (e.g. One day that is either a Sydney Business Day or a Melbourne Business Day following the Reset Date)")
  """
  Legal text that underlies the Fixing Offset. ISDA Fixing Offset Definition. (e.g. One day that is either a Sydney Business Day or a Melbourne Business Day following the Reset Date)
  """
  fixingOffsetReason: Optional[str] = Field(None, description="Fixing Offset Reason")
  """
  Fixing Offset Reason
  """

from cdm.base.datetime.BusinessCenters import BusinessCenters

BusinessDayOffset.update_forward_refs()
