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

__all__ = ['TradeState']


class TradeState(BaseDataClass):
  """
  Defines the fundamental financial information that can be changed by a Primitive Event and by extension any business or life-cycle event. Each TradeState specifies where a Trade is in its life-cycle. TradeState is a root type and as such, can be created independently to any other CDM data type, but can also be used as part of the CDM Event Model.
  """
  observationHistory: List[ObservationEvent] = Field([], description="Represents the observed events related to a particular product or process, such as credit events or corporate actions.")
  """
  Represents the observed events related to a particular product or process, such as credit events or corporate actions.
  """
  resetHistory: List[Reset] = Field([], description="Represents the updated Trade attributes which can change as the result of a reset event. Only the changed values are captured, leaving the remaining data attributes empty. See Create_Reset function for further details on how TradeState is used in the Reset event. The TradeState data type is used to maintain backwards compatibility with the current Reset mechanism.")
  """
  Represents the updated Trade attributes which can change as the result of a reset event. Only the changed values are captured, leaving the remaining data attributes empty. See Create_Reset function for further details on how TradeState is used in the Reset event. The TradeState data type is used to maintain backwards compatibility with the current Reset mechanism.
  """
  state: Optional[State] = Field(None, description="Represents the State of the Trade through its life-cycle.")
  """
  Represents the State of the Trade through its life-cycle.
  """
  trade: Trade = Field(..., description="Represents the Trade that has been effected by a business or life-cycle event.")
  """
  Represents the Trade that has been effected by a business or life-cycle event.
  """
  transferHistory: List[TransferState] = Field([], description="Represents the updated Trade attributes which can change as the result of a transfer event.")
  """
  Represents the updated Trade attributes which can change as the result of a transfer event.
  """

from cdm.event.common.ObservationEvent import ObservationEvent
from cdm.event.common.Reset import Reset
from cdm.event.common.State import State
from cdm.event.common.Trade import Trade
from cdm.event.common.TransferState import TransferState

TradeState.update_forward_refs()
