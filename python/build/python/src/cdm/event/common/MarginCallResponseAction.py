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

__all__ = ['MarginCallResponseAction']


class MarginCallResponseAction(BaseDataClass):
  """
  Specifies the margin call action details, including collateral to be moved and its direction.
  """
  collateralPositionComponent: List[CollateralPosition] = Field([], description="Specifies the collateral to be moved and its direction.")
  """
  Specifies the collateral to be moved and its direction.
  """
  @rosetta_condition
  def cardinality_collateralPositionComponent(self):
    return check_cardinality(self.collateralPositionComponent, 1, None)
  
  marginCallAction: MarginCallActionEnum = Field(..., description="Specifies the margin call action details, specified as either Delivery or Return.")
  """
  Specifies the margin call action details, specified as either Delivery or Return.
  """

from cdm.event.common.CollateralPosition import CollateralPosition
from cdm.event.common.MarginCallActionEnum import MarginCallActionEnum

MarginCallResponseAction.update_forward_refs()
