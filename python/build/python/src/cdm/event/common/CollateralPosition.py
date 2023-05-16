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

__all__ = ['CollateralPosition']

from cdm.event.position.Position import Position

class CollateralPosition(Position):
  """
  Specifies the individual components of collateral positions.
  """
  collateralPositionStatus: Optional[CollateralStatusEnum] = Field(None, description="Indicates the collateral positions settlement status.")
  """
  Indicates the collateral positions settlement status.
  """
  treatment: Optional[CollateralTreatment] = Field(None, description="Specifies if there is any treatment to be applied to collateral, such as percentage discount which will impact collateral value.")
  """
  Specifies if there is any treatment to be applied to collateral, such as percentage discount which will impact collateral value.
  """
  
  @rosetta_condition
  def condition_0_CollateralPositionStatusSettledOrInTransitOnly(self):
    """
    Represents a condition to ensure that if a status is defined for a collateral position you must only indicate 'Settled Amount' or 'In Transit' amount from the available enumerations.
    """
    def _then_fn0():
      return (all_elements(self.collateralPositionStatus, "=", CollateralStatusEnum.SETTLED_AMOUNT) or all_elements(self.collateralPositionStatus, "=", CollateralStatusEnum.IN_TRANSIT_AMOUNT))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.collateralPositionStatus) is not None), _then_fn0, _else_fn0)

from cdm.event.common.CollateralStatusEnum import CollateralStatusEnum
from cdm.legaldocumentation.csa.CollateralTreatment import CollateralTreatment

CollateralPosition.update_forward_refs()
