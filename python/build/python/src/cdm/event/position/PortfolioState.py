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

__all__ = ['PortfolioState']


class PortfolioState(BaseDataClass):
  """
  State-full representation of a Portfolio that describes all the positions held at a given time, in various states which can be either traded, settled, etc., with lineage information to the previous state
  """
  lineage: Lineage = Field(..., description="Pointer to the previous PortfolioState and new Event(s) leading to the current (new) state. Previous PortfolioState in the Lineage can be Null in case this is the start of the chain of Events.")
  """
  Pointer to the previous PortfolioState and new Event(s) leading to the current (new) state. Previous PortfolioState in the Lineage can be Null in case this is the start of the chain of Events.
  """
  positions: List[Position] = Field([], description="The list of positions, each containing a Quantity and a Product.")
  """
  The list of positions, each containing a Quantity and a Product.
  """
  
  @rosetta_condition
  def condition_0_Initialisation(self):
    """
    When the PortfolioState is the starting state of the Portfolio, as identified by a Null state in the Lineage, Positions must be empty and the reference to the latest Event is also empty. This is how a Portfolio gets initialised.
    """
    def _then_fn0():
      return (((self.positions) is None) and ((self.lineage.eventReference) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.lineage.portfolioStateReference) is None), _then_fn0, _else_fn0)

from cdm.event.common.Lineage import Lineage
from cdm.event.position.Position import Position

PortfolioState.update_forward_refs()
