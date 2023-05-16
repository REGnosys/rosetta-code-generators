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

__all__ = ['TradeLot']


class TradeLot(BaseDataClass):
  """
  Specifies the price and quantity of a trade lot, where the same product could be traded multiple times with the same counterparty but in different lots (at a different date, in a different quantity and at a different price). One trade lot combined with a product definition specifies the entire economics of a trade. The lifecycle mechanics of each such trade lot (e.g. cashflow payments) is independent of the other lots.
  """
  lotIdentifier: List[Identifier] = Field([], description="Specifies one or more identifiers for the lot, if any.")
  """
  Specifies one or more identifiers for the lot, if any.
  """
  priceQuantity: List[PriceQuantity] = Field([], description="Specifies the settlement characteristics of a trade lot: price, quantity, observable (optionally) and the settlement terms. This attribute has a multiple cardinality to allow to specify the price, quantity and observable of different legs in a single, composite product (e.g. a Swap).")
  """
  Specifies the settlement characteristics of a trade lot: price, quantity, observable (optionally) and the settlement terms. This attribute has a multiple cardinality to allow to specify the price, quantity and observable of different legs in a single, composite product (e.g. a Swap).
  """
  @rosetta_condition
  def cardinality_priceQuantity(self):
    return check_cardinality(self.priceQuantity, 1, None)
  

from cdm.base.staticdata.identifier.Identifier import Identifier
from cdm.product.common.settlement.PriceQuantity import PriceQuantity

TradeLot.update_forward_refs()
