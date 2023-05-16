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

__all__ = ['PartyChangeInstruction']


class PartyChangeInstruction(BaseDataClass):
  """
  Specifies instruction to change the party on a trade. This primitive instruction is used in a number of scenarios including: clearing, allocation and novation. The instrution must include a trade identifier, because a change of party effectively results in a different trade.
  """
  ancillaryParty: Optional[AncillaryParty] = Field(None, description="Specifies an ancillary party to be added onto the new transaction, e.g. the original executing party in an allocation.")
  """
  Specifies an ancillary party to be added onto the new transaction, e.g. the original executing party in an allocation.
  """
  counterparty: Counterparty = Field(..., description="The new counterparty who is stepping into the trade. The stepping out counterparty is inferred based on the counterparty role that is being updated.")
  """
  The new counterparty who is stepping into the trade. The stepping out counterparty is inferred based on the counterparty role that is being updated.
  """
  partyRole: Optional[PartyRole] = Field(None, description="Specifies an additional party roles to be added on to the new transaction.")
  """
  Specifies an additional party roles to be added on to the new transaction.
  """
  tradeId: List[Identifier] = Field([], description="The identifier to be assigned to the new trade post change of party.")
  """
  The identifier to be assigned to the new trade post change of party.
  """
  @rosetta_condition
  def cardinality_tradeId(self):
    return check_cardinality(self.tradeId, 1, None)
  

from cdm.base.staticdata.party.AncillaryParty import AncillaryParty
from cdm.base.staticdata.party.Counterparty import Counterparty
from cdm.base.staticdata.party.PartyRole import PartyRole
from cdm.base.staticdata.identifier.Identifier import Identifier

PartyChangeInstruction.update_forward_refs()
