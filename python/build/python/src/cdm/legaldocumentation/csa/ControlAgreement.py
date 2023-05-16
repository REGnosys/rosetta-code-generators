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

__all__ = ['ControlAgreement']


class ControlAgreement(BaseDataClass):
  """
  A class to specify the relationship between the Control Agreement and the Credit Support Agreement.
  """
  partyElection: List[ControlAgreementElections] = Field([], description="The party specific elections.")
  """
  The party specific elections.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 2, 2)
  

from cdm.legaldocumentation.csa.ControlAgreementElections import ControlAgreementElections

ControlAgreement.update_forward_refs()
