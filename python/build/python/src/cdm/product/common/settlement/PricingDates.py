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

__all__ = ['PricingDates']


class PricingDates(BaseDataClass):
  """
  Specifies specific dates or parametric rules for the dates on which the price will be determined
  """
  parametricDates: Optional[ParametricDates] = Field(None, description="Defines rules for the dates on which the price will be determined.")
  """
  Defines rules for the dates on which the price will be determined.
  """
  specifiedDates: List[AdjustableDates] = Field([], description="Defines specified dates on which the price will be determined.")
  """
  Defines specified dates on which the price will be determined.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('specifiedDates', 'parametricDates', necessity=True)

from cdm.product.common.schedule.ParametricDates import ParametricDates
from cdm.base.datetime.AdjustableDates import AdjustableDates

PricingDates.update_forward_refs()
