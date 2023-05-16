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

__all__ = ['State']


class State(BaseDataClass):
  """
  Defines the state of a trade at a point in the Trade's life cycle. Trades have many state dimensions, all of which are represented here. For example, states useful for position keeping are represented alongside those needed for regulatory reporting.
  """
  closedState: Optional[ClosedState] = Field(None, description="Represents the qualification of what led to the trade's closure alongside the dates on which this closure took effect.")
  """
  Represents the qualification of what led to the trade's closure alongside the dates on which this closure took effect.
  """
  positionState: Optional[PositionStatusEnum] = Field(None, description="Identifies the state of the position, to distinguish if just executed, formed, already settled, closed, etc.")
  """
  Identifies the state of the position, to distinguish if just executed, formed, already settled, closed, etc.
  """
  
  @rosetta_condition
  def condition_0_ClosedStateExists(self):
    """
    When the position state is identified as closed, the closed state must also be specified.
    """
    def _then_fn0():
      return ((self.closedState) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.positionState, "=", PositionStatusEnum.CLOSED), _then_fn0, _else_fn0)

from cdm.legaldocumentation.common.ClosedState import ClosedState
from cdm.event.position.PositionStatusEnum import PositionStatusEnum

State.update_forward_refs()
