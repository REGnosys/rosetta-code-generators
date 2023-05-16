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

__all__ = ['NumberRange']


class NumberRange(BaseDataClass):
  """
  The number range defined as either a lower and upper number bound, or both.
  """
  lowerBound: Optional[NumberBound] = Field(None, description="The lower bound of a number range, e.g. greater than or equal to 5.")
  """
  The lower bound of a number range, e.g. greater than or equal to 5.
  """
  upperBound: Optional[NumberBound] = Field(None, description="The upper bound of a number range, e.g. less than 10.")
  """
  The upper bound of a number range, e.g. less than 10.
  """
  
  @rosetta_condition
  def condition_0_AtLeastOneOf(self):
    return (((self.lowerBound) is not None) or ((self.upperBound) is not None))

from cdm.base.math.NumberBound import NumberBound

NumberRange.update_forward_refs()
