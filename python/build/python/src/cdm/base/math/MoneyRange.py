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

__all__ = ['MoneyRange']


class MoneyRange(BaseDataClass):
  """
  The money range defined as either a lower and upper money bound, or both.
  """
  lowerBound: Optional[MoneyBound] = Field(None, description="The lower bound of a money range, e.g. greater than or equal to 1,000 USD.")
  """
  The lower bound of a money range, e.g. greater than or equal to 1,000 USD.
  """
  upperBound: Optional[MoneyBound] = Field(None, description="The upper bound of a money range, e.g. less than 10,000 USD.")
  """
  The upper bound of a money range, e.g. less than 10,000 USD.
  """
  
  @rosetta_condition
  def condition_0_AtLeastOneOf(self):
    return (((self.lowerBound) is not None) or ((self.upperBound) is not None))

from cdm.base.math.MoneyBound import MoneyBound

MoneyRange.update_forward_refs()
