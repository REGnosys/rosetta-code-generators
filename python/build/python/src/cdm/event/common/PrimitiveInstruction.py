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

__all__ = ['PrimitiveInstruction']


class PrimitiveInstruction(BaseDataClass):
  """
  A Primitive Instruction describes the inputs required to pass into the corresponding PrimitiveEvent function.
  """
  contractFormation: Optional[ContractFormationInstruction] = Field(None, description="Specifies instructions describing an contract formation primitive event.")
  """
  Specifies instructions describing an contract formation primitive event.
  """
  execution: Optional[ExecutionInstruction] = Field(None, description="Specifies instructions describing an execution primitive event.")
  """
  Specifies instructions describing an execution primitive event.
  """
  exercise: Optional[ExerciseInstruction] = Field(None, description="Specifies instructions describing an exercise primitive event.")
  """
  Specifies instructions describing an exercise primitive event.
  """
  indexTransition: Optional[IndexTransitionInstruction] = Field(None, description="Specifies inputs needed to process a Index Transition business event.")
  """
  Specifies inputs needed to process a Index Transition business event.
  """
  observation: Optional[ObservationInstruction] = Field(None, description="Specifies inputs needed to process an observation.")
  """
  Specifies inputs needed to process an observation.
  """
  partyChange: Optional[PartyChangeInstruction] = Field(None, description="Specifies instructions describing a party change primitive event.")
  """
  Specifies instructions describing a party change primitive event.
  """
  quantityChange: Optional[QuantityChangeInstruction] = Field(None, description="Specifies instructions describing an quantity change primitive event.")
  """
  Specifies instructions describing an quantity change primitive event.
  """
  reset: Optional[ResetInstruction] = Field(None, description="Specifies instructions describing a reset event.")
  """
  Specifies instructions describing a reset event.
  """
  split: Optional[SplitInstruction] = Field(None, description="Specifies instructions to split a trade into multiple branches.")
  """
  Specifies instructions to split a trade into multiple branches.
  """
  stockSplit: Optional[StockSplitInstruction] = Field(None, description="Specifies inputs needed to process a Stock Split business event.")
  """
  Specifies inputs needed to process a Stock Split business event.
  """
  termsChange: Optional[TermsChangeInstruction] = Field(None, description="Specifies instructions describing a terms change primitive event.")
  """
  Specifies instructions describing a terms change primitive event.
  """
  transfer: Optional[TransferInstruction] = Field(None, description="Specifies instructions describing a transfer primitive event.")
  """
  Specifies instructions describing a transfer primitive event.
  """

from cdm.event.common.ContractFormationInstruction import ContractFormationInstruction
from cdm.event.common.ExecutionInstruction import ExecutionInstruction
from cdm.event.common.ExerciseInstruction import ExerciseInstruction
from cdm.event.common.IndexTransitionInstruction import IndexTransitionInstruction
from cdm.event.common.ObservationInstruction import ObservationInstruction
from cdm.event.common.PartyChangeInstruction import PartyChangeInstruction
from cdm.event.common.QuantityChangeInstruction import QuantityChangeInstruction
from cdm.event.common.ResetInstruction import ResetInstruction
from cdm.event.common.SplitInstruction import SplitInstruction
from cdm.event.common.StockSplitInstruction import StockSplitInstruction
from cdm.event.common.TermsChangeInstruction import TermsChangeInstruction
from cdm.event.common.TransferInstruction import TransferInstruction

PrimitiveInstruction.update_forward_refs()
