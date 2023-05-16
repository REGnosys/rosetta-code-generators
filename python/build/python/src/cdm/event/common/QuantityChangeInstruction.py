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

__all__ = ['QuantityChangeInstruction']


class QuantityChangeInstruction(BaseDataClass):
  """
  Instructions required to create a Quantity Change Primitive Event, which can be either an increase, a decrease or a replacement. An increase adds a new trade lot to the original trade, whereas a decrease subtracts from an existing trade lot's quantity. A replacement updates the quantity of an existing trade lot to the new value.
  """
  change: List[PriceQuantity] = Field([], description="Quantity by which the trade is being increased, decreased or replaced, and the price at which such quantity change is agreed. The quantity change should always be specified as a positive number, with the direction (increase/decrease/replacement) being specified by the direction enumeration. A fee can also be associated to the quantity change by specifying a Price component of type CashPrice, including the corresponding settlement date and direction.")
  """
  Quantity by which the trade is being increased, decreased or replaced, and the price at which such quantity change is agreed. The quantity change should always be specified as a positive number, with the direction (increase/decrease/replacement) being specified by the direction enumeration. A fee can also be associated to the quantity change by specifying a Price component of type CashPrice, including the corresponding settlement date and direction.
  """
  @rosetta_condition
  def cardinality_change(self):
    return check_cardinality(self.change, 1, None)
  
  direction: QuantityChangeDirectionEnum = Field(..., description="Direction of the quantity change specified as either an increase, decrease or replacement.")
  """
  Direction of the quantity change specified as either an increase, decrease or replacement.
  """
  lotIdentifier: List[Identifier] = Field([], description="Identifier for the new lot (in case of increase) or for the existing lot to be changed(in case of decrease or replacement). This optional attribute is mandatory in case of a decrease or replacement if the initial trade state contains multiple trade lots.")
  """
  Identifier for the new lot (in case of increase) or for the existing lot to be changed(in case of decrease or replacement). This optional attribute is mandatory in case of a decrease or replacement if the initial trade state contains multiple trade lots.
  """

from cdm.product.common.settlement.PriceQuantity import PriceQuantity
from cdm.base.math.QuantityChangeDirectionEnum import QuantityChangeDirectionEnum
from cdm.base.staticdata.identifier.Identifier import Identifier

QuantityChangeInstruction.update_forward_refs()
