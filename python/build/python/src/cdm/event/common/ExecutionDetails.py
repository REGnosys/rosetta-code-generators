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

__all__ = ['ExecutionDetails']


class ExecutionDetails(BaseDataClass):
  """
  Defines specific attributes that relate to trade executions.
  """
  executionType: ExecutionTypeEnum = Field(..., description="Identifies the type of execution, e.g. via voice, electronically...")
  """
  Identifies the type of execution, e.g. via voice, electronically...
  """
  executionVenue: Optional[LegalEntity] = Field(None, description="Represents the venue on which a trade was executed.")
  """
  Represents the venue on which a trade was executed.
  """
  packageReference: Optional[AttributeWithReference | IdentifiedList] = Field(None, description="A reference to the package linking the trade with other trades, in case the trade was executed as part of a package (hence this attribute is optional).")
  """
  A reference to the package linking the trade with other trades, in case the trade was executed as part of a package (hence this attribute is optional).
  """
  
  @rosetta_condition
  def condition_0_ExecutionVenue(self):
    """
    When the execution type is set to 'Electronically', the execution venue must be specified.
    """
    def _then_fn0():
      return ((self.executionVenue) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.executionType, "=", ExecutionTypeEnum.ELECTRONIC), _then_fn0, _else_fn0)

from cdm.event.common.ExecutionTypeEnum import ExecutionTypeEnum
from cdm.base.staticdata.party.LegalEntity import LegalEntity
from cdm.base.staticdata.identifier.IdentifiedList import IdentifiedList

ExecutionDetails.update_forward_refs()
