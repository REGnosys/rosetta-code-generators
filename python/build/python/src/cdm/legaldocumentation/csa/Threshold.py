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

__all__ = ['Threshold']


class Threshold(BaseDataClass):
  """
  A class to specify the unsecured credit exposure that each party to the agreement is prepared to accept before asking for collateral. This threshold is specified either as an amount or as a custom election. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (c)(vi)(A): Threshold. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(vi)(A): Threshold. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (c)(vi)(A): Threshold.
  """
  partyElection: List[ElectiveAmountElection] = Field([], description="The parties' Threshold election.")
  """
  The parties' Threshold election.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 2, 2)
  

from cdm.legaldocumentation.csa.ElectiveAmountElection import ElectiveAmountElection

Threshold.update_forward_refs()
