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

__all__ = ['RateSchedule']


class RateSchedule(BaseDataClass):
  """
  A class defining a schedule of rates or amounts in terms of an initial value and then a series of step date and value pairs. On each step date the rate or amount changes to the new step value. The series of step date and value pairs are optional. If not specified, this implies that the initial value remains unchanged over time.
  """
  price: AttributeWithAddress[PriceSchedule] | PriceSchedule = Field(..., description="The initial rate. An initial rate of 5% would be represented as 0.05.")
  """
  The initial rate. An initial rate of 5% would be represented as 0.05.
  """

from cdm.observable.asset.PriceSchedule import PriceSchedule

RateSchedule.update_forward_refs()
