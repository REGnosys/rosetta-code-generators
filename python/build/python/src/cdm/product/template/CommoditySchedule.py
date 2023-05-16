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

__all__ = ['CommoditySchedule']


class CommoditySchedule(BaseDataClass):
  """
  A class that allows the full representation of a commodity payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.
  """
  schedulePeriod: List[SchedulePeriod] = Field([], description="Defines a period of a commodity schedule structure.")
  """
  Defines a period of a commodity schedule structure.
  """
  @rosetta_condition
  def cardinality_schedulePeriod(self):
    return check_cardinality(self.schedulePeriod, 1, None)
  

from cdm.product.template.SchedulePeriod import SchedulePeriod

CommoditySchedule.update_forward_refs()
