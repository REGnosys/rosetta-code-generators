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

__all__ = ['Custodian']


class Custodian(BaseDataClass):
  """
  A class to specify the custodian and custody account details for each party to the agreement.
  """
  partyElection: List[CustodianElection] = Field([], description="The party specific elections.")
  """
  The party specific elections.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 2, 2)
  

from cdm.legaldocumentation.csa.CustodianElection import CustodianElection

Custodian.update_forward_refs()
