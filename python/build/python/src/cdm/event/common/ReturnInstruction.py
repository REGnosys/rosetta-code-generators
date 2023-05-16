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

__all__ = ['ReturnInstruction']


class ReturnInstruction(BaseDataClass):
  """
  Specifies the information required to create the return of a Security Finance Transaction.
  """
  quantity: List[Quantity] = Field([], description="Specifies the quantity of shares and cash to be returned in a partial return event.")
  """
  Specifies the quantity of shares and cash to be returned in a partial return event.
  """
  @rosetta_condition
  def cardinality_quantity(self):
    return check_cardinality(self.quantity, 1, None)
  

from cdm.base.math.Quantity import Quantity

ReturnInstruction.update_forward_refs()
