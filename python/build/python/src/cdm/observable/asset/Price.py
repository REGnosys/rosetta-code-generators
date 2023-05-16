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

__all__ = ['Price']

from cdm.observable.asset.PriceSchedule import PriceSchedule

class Price(PriceSchedule):
  """
  Specifies a price as a single value to be associated to a financial product. This data type extends PriceSchedule and requires that only the amount value exists.
  """
  
  @rosetta_condition
  def condition_0_AmountOnlyExists(self):
    """
    The amount must exist when the price represents a single value, and steps must be absent.
    """
    return (((self.value) is not None) and ((self.datedValue) is None))


Price.update_forward_refs()
