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

__all__ = ['SchedulePeriod']


class SchedulePeriod(BaseDataClass):
  """
  A class that defines the commodity period of a schedule. The period contains a set of start and end dates, quantities, fixing, and pricing data.
  """
  calculationPeriod: DateRange = Field(..., description="Period for which the payment is generated.")
  """
  Period for which the payment is generated.
  """
  fixingPeriod: DateRange = Field(..., description="Period over which the underlying price is observed.")
  """
  Period over which the underlying price is observed.
  """
  paymentDate: date = Field(..., description="Adjusted payment date.")
  """
  Adjusted payment date.
  """

from cdm.base.datetime.DateRange import DateRange

SchedulePeriod.update_forward_refs()
