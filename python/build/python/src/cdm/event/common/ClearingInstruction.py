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

__all__ = ['ClearingInstruction']


class ClearingInstruction(BaseDataClass):
  """
  All information required to perform the clear life cycle event; the clearing party (CCP), the two parties facing each other on the alpha contract, and optionally the parties acting as clearing members.
  """
  alphaContract: TradeState = Field(..., description="The contract that will be submitted to the clearing house for clearing. The contract should indicate that it should be cleared by assigning a clearing organisation as a party role.")
  """
  The contract that will be submitted to the clearing house for clearing. The contract should indicate that it should be cleared by assigning a clearing organisation as a party role.
  """
  clearerParty1: Optional[Party] = Field(None, description="Optional party facing the CCP, acting as clearing member for party1.")
  """
  Optional party facing the CCP, acting as clearing member for party1.
  """
  clearerParty2: Optional[Party] = Field(None, description="Optional party facing the CCP, acting as clearing member for party2.")
  """
  Optional party facing the CCP, acting as clearing member for party2.
  """
  clearingParty: Party = Field(..., description="The Central Counter party (CCP) that the contract will be submitted to for clearing.")
  """
  The Central Counter party (CCP) that the contract will be submitted to for clearing.
  """
  party1: Party = Field(..., description="First party facing the CCP if it is clearing for its own account.")
  """
  First party facing the CCP if it is clearing for its own account.
  """
  party2: Party = Field(..., description="Second party facing the CCP if it is clearing for its own account.")
  """
  Second party facing the CCP if it is clearing for its own account.
  """

from cdm.event.common.TradeState import TradeState
from cdm.base.staticdata.party.Party import Party

ClearingInstruction.update_forward_refs()
