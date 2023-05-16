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

__all__ = ['Position']


class Position(BaseDataClass):
  """
  A Position describes how much of a given Product is being held and constitutes the atomic element of a Portfolio.
  """
  cashBalance: Optional[Money] = Field(None, description="The aggregate cost of proceeds")
  """
  The aggregate cost of proceeds
  """
  positionComponent: List[PriceQuantity] = Field([], description="Position with many price quantities.")
  """
  Position with many price quantities.
  """
  @rosetta_condition
  def cardinality_positionComponent(self):
    return check_cardinality(self.positionComponent, 1, None)
  
  tradeReference: Optional[AttributeWithReference | TradeState] = Field(None, description="Reference to the Contract, in case product is contractual and the contract has been formed")
  """
  Reference to the Contract, in case product is contractual and the contract has been formed
  """

from cdm.observable.asset.Money import Money
from cdm.product.common.settlement.PriceQuantity import PriceQuantity
from cdm.event.common.TradeState import TradeState

Position.update_forward_refs()
