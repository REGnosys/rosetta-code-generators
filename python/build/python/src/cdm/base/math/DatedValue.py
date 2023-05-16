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

__all__ = ['DatedValue']


class DatedValue(BaseDataClass):
  """
  Defines a date and value pair. This definition is used for varying rate or amount schedules, e.g. a notional amortisation or a step-up coupon schedule.
  """
  date: date = Field(..., description="The date on which the associated step value becomes effective. This day may be subject to adjustment in accordance with a business day convention.")
  """
  The date on which the associated step value becomes effective. This day may be subject to adjustment in accordance with a business day convention.
  """
  value: Decimal = Field(..., description="The rate of amount which becomes effective on the associated step date. A rate of 5% would be represented as 0.05.")
  """
  The rate of amount which becomes effective on the associated step date. A rate of 5% would be represented as 0.05.
  """


DatedValue.update_forward_refs()
