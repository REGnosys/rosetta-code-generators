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

__all__ = ['ObservationEvent']


class ObservationEvent(BaseDataClass):
  """
  Specifies the necessary information to create any observation event.
  """
  corporateAction: Optional[CorporateAction] = Field(None, description="Specifies the necessary information to create a corporate action.")
  """
  Specifies the necessary information to create a corporate action.
  """
  creditEvent: Optional[CreditEvent] = Field(None, description="Specifies the necessary information to create a credit event.")
  """
  Specifies the necessary information to create a credit event.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('creditEvent', 'corporateAction', necessity=True)

from cdm.event.common.CorporateAction import CorporateAction
from cdm.event.common.CreditEvent import CreditEvent

ObservationEvent.update_forward_refs()
