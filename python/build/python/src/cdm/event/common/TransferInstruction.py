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

__all__ = ['TransferInstruction']


class TransferInstruction(BaseDataClass):
  """
  Defines the payout on which to create a Transfer along with all necessary resets.
  """
  transferState: List[TransferState] = Field([], description="Specifies the terms and state of a transfers.")
  """
  Specifies the terms and state of a transfers.
  """

from cdm.event.common.TransferState import TransferState

TransferInstruction.update_forward_refs()
