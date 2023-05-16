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

__all__ = ['Rounding']


class Rounding(BaseDataClass):
  """
  Defines rounding rules and precision to be used in the rounding of a number.
  """
  precision: Optional[int] = Field(None, description="Specifies the rounding precision in terms of a number of decimal places when the number is evaluated in decimal form (not percentage), e.g. 0.09876543 rounded to the nearest 5 decimal places is  0.0987654.")
  """
  Specifies the rounding precision in terms of a number of decimal places when the number is evaluated in decimal form (not percentage), e.g. 0.09876543 rounded to the nearest 5 decimal places is  0.0987654.
  """
  roundingDirection: RoundingDirectionEnum = Field(..., description="Specifies the rounding rounding rule as up, down, or nearest.")
  """
  Specifies the rounding rounding rule as up, down, or nearest.
  """

from cdm.base.math.RoundingDirectionEnum import RoundingDirectionEnum

Rounding.update_forward_refs()
