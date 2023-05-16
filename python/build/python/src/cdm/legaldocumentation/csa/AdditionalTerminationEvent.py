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

__all__ = ['AdditionalTerminationEvent']


class AdditionalTerminationEvent(BaseDataClass):
  """
  A class to specify an optional termination event, additional to the Termination Events that will be deemed an Access Condition (Initial Margin CSA) or a Specified Condition (Variation Margin CSA)
  """
  applicableParty: List[CounterpartyRoleEnum] = Field([], description="Whether the additional termination event is applicable for the relevant party")
  """
  Whether the additional termination event is applicable for the relevant party
  """
  @rosetta_condition
  def cardinality_applicableParty(self):
    return check_cardinality(self.applicableParty, 1, 2)
  
  name: str = Field(..., description="The name of the additional termination event")
  """
  The name of the additional termination event
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

AdditionalTerminationEvent.update_forward_refs()
