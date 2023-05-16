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

__all__ = ['Money']

from cdm.base.math.Quantity import Quantity

class Money(Quantity):
  """
  Defines a monetary amount in a specified currency.
  """
  
  @rosetta_condition
  def condition_0_CurrencyUnitExists(self):
    return ((self.unit.currency) is not None)


Money.update_forward_refs()
