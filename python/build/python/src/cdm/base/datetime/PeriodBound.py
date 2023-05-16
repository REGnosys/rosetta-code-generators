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

__all__ = ['PeriodBound']


class PeriodBound(BaseDataClass):
  """
  Indicator to specify if the period bound is defined as a period and whether the bound is inclusive.
  """
  inclusive: bool = Field(..., description="Specifies whether the period bound is inclusive, e.g. for a lower bound, false would indicate greater than, whereas true would indicate greater than or equal to.")
  """
  Specifies whether the period bound is inclusive, e.g. for a lower bound, false would indicate greater than, whereas true would indicate greater than or equal to.
  """
  period: Period = Field(..., description="Specifies the period is to be used as the bound, e.g. 5Y.")
  """
  Specifies the period is to be used as the bound, e.g. 5Y.
  """

from cdm.base.datetime.Period import Period

PeriodBound.update_forward_refs()
