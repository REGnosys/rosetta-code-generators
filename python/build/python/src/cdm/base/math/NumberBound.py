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

__all__ = ['NumberBound']


class NumberBound(BaseDataClass):
  """
  The number bound is defined as a number and whether the bound is inclusive.
  """
  inclusive: bool = Field(..., description="Whether the number bound is inclusive, e.g. for a lower bound, false would indicate greater than, whereas true would indicate greater than or equal to.")
  """
  Whether the number bound is inclusive, e.g. for a lower bound, false would indicate greater than, whereas true would indicate greater than or equal to.
  """
  number: Decimal = Field(..., description="The number to be used as the bound, e.g. 5.")
  """
  The number to be used as the bound, e.g. 5.
  """


NumberBound.update_forward_refs()
