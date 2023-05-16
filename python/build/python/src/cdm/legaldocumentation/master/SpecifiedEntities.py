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

__all__ = ['SpecifiedEntities']


class SpecifiedEntities(BaseDataClass):
  """
  A provision that allows each party to specify its Specified Entities for certain Events of Default and Termination Events
  """
  specifiedEntity: List[SpecifiedEntity] = Field([], description="The party specific election of Specified Entities for the Event of Default or Termination Event specified.")
  """
  The party specific election of Specified Entities for the Event of Default or Termination Event specified.
  """
  @rosetta_condition
  def cardinality_specifiedEntity(self):
    return check_cardinality(self.specifiedEntity, 2, 2)
  
  specifiedEntityClause: SpecifiedEntityClauseEnum = Field(..., description="The Event of Default or Termination event for which Specified Entities terms are being defined.")
  """
  The Event of Default or Termination event for which Specified Entities terms are being defined.
  """

from cdm.legaldocumentation.master.SpecifiedEntity import SpecifiedEntity
from cdm.legaldocumentation.common.SpecifiedEntityClauseEnum import SpecifiedEntityClauseEnum

SpecifiedEntities.update_forward_refs()
