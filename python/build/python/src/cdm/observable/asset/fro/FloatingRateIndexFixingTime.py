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

__all__ = ['FloatingRateIndexFixingTime']

from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime

class FloatingRateIndexFixingTime(BusinessCenterTime):
  """
  This type holds parameters defining the normal fixing time for a floating rate index.
  """
  designatedMaturity: Optional[str] = Field(None, description="Allows a designed maturity to be specified for the fixing time.")
  """
  Allows a designed maturity to be specified for the fixing time.
  """
  fixingReason: Optional[str] = Field(None, description="Fixing Reason")
  """
  Fixing Reason
  """
  fixingTimeDefinition: Optional[str] = Field(None, description="Legal text that underlies the Fixing Time. ISDA Fixing Time Definition. (e.g. 09:30, Sydney time).")
  """
  Legal text that underlies the Fixing Time. ISDA Fixing Time Definition. (e.g. 09:30, Sydney time).
  """


FloatingRateIndexFixingTime.update_forward_refs()
