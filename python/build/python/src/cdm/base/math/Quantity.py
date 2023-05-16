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

__all__ = ['Quantity']

from cdm.base.math.QuantitySchedule import QuantitySchedule

class Quantity(QuantitySchedule):
  """
  Specifies a quantity as a single value to be associated to a financial product, for example a transfer amount resulting from a trade. This data type extends QuantitySchedule and requires that only the single amount value exists.
  """
  
  @rosetta_condition
  def condition_0_AmountOnlyExists(self):
    """
    The amount must exist when the quantity represents a single value, and the steps must be absent.
    """
    return (((self.value) is not None) and ((self.datedValue) is None))


Quantity.update_forward_refs()
