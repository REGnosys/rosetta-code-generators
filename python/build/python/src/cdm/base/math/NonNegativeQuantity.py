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

__all__ = ['NonNegativeQuantity']

from cdm.base.math.Quantity import Quantity

class NonNegativeQuantity(Quantity):
  """
  Specifies a quantity as a non-negative number, which condition is enforced through a data rule that only applies to the extending class.
  """
  
  @rosetta_condition
  def condition_0_NonNegativeQuantity_amount(self):
    """
    For a non-negative quantity, the amount attribute must be positive.
    """
    return all_elements(self.value, ">=", 0.0)


NonNegativeQuantity.update_forward_refs()
