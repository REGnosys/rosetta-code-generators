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

__all__ = ['TransferState']


class TransferState(BaseDataClass):
  """
  Defines the fundamental financial information associated with a Transfer event. Each TransferState specifies where a Transfer is in its life-cycle. TransferState is a root type and as such, can be created independently to any other CDM data type, but can also be used as part of the CDM Event Model.
  """
  transfer: Transfer = Field(..., description="Represents the Transfer that has been effected by a business or life-cycle event.")
  """
  Represents the Transfer that has been effected by a business or life-cycle event.
  """
  transferStatus: Optional[TransferStatusEnum] = Field(None, description="Represents the State of the Transfer through its life-cycle.")
  """
  Represents the State of the Transfer through its life-cycle.
  """

from cdm.event.common.Transfer import Transfer
from cdm.event.common.TransferStatusEnum import TransferStatusEnum

TransferState.update_forward_refs()
