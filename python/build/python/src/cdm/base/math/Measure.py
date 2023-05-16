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

__all__ = ['Measure']

from cdm.base.math.MeasureBase import MeasureBase

class Measure(MeasureBase):
  """
  Defines a concrete measure as a number associated to a unit. It extends MeasureBase by requiring the value attribute to be present. A measure may be unit-less so the unit attribute is still optional.
  """
  
  @rosetta_condition
  def condition_0_ValueExists(self):
    """
    The value attribute must be present in a concrete measure.
    """
    return ((self.value) is not None)


Measure.update_forward_refs()
