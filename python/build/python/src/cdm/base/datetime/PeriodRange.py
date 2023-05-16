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

__all__ = ['PeriodRange']


class PeriodRange(BaseDataClass):
  """
  Indicates The period range defined as either a lower and upper period bound, or both.
  """
  lowerBound: Optional[PeriodBound] = Field(None, description="Specifies the lower bound of a period range, e.g. greater than or equal to 5Y.")
  """
  Specifies the lower bound of a period range, e.g. greater than or equal to 5Y.
  """
  upperBound: Optional[PeriodBound] = Field(None, description="Specifies the upper bound of a period range, e.g. less than to 10Y.")
  """
  Specifies the upper bound of a period range, e.g. less than to 10Y.
  """
  
  @rosetta_condition
  def condition_0_AtLeastOneOf(self):
    return (((self.lowerBound) is not None) or ((self.upperBound) is not None))

from cdm.base.datetime.PeriodBound import PeriodBound

PeriodRange.update_forward_refs()
