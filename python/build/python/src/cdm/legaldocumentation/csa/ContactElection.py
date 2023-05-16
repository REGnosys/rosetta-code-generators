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

__all__ = ['ContactElection']


class ContactElection(BaseDataClass):
  """
  A class to specify the parties' election to specify contact information, in relation to elections such as the Addresses for Transfer or the Demand and Notices as specified in the ISDA Credit Support Annex agreement.
  """
  partyElection: List[PartyContactInformation] = Field([], description="The parties' contact information election.")
  """
  The parties' contact information election.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 2, 2)
  

from cdm.base.staticdata.party.PartyContactInformation import PartyContactInformation

ContactElection.update_forward_refs()
