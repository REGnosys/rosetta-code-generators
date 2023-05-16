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

__all__ = ['AdditionalRepresentation']


class AdditionalRepresentation(BaseDataClass):
  """
  A class to specify the Additional Representation. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (o): Additional Representation(s).
  """
  customElection: Optional[str] = Field(None, description="A supplemental custom election that might be specified by the parties for the purpose of specifying the Additional Representation.")
  """
  A supplemental custom election that might be specified by the parties for the purpose of specifying the Additional Representation.
  """
  partyElection: List[AdditionalRepresentationElection] = Field([], description="A qualification as to whether the Additional Representation is applicable.")
  """
  A qualification as to whether the Additional Representation is applicable.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 2, 2)
  

from cdm.legaldocumentation.csa.AdditionalRepresentationElection import AdditionalRepresentationElection

AdditionalRepresentation.update_forward_refs()
