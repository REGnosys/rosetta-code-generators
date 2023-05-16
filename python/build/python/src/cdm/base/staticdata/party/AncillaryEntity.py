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

__all__ = ['AncillaryEntity']


class AncillaryEntity(BaseDataClass):
  """
  Holds an identifier for an ancillary entity, either identified directly via its ancillary role or directly as a legal entity.
  """
  ancillaryParty: Optional[AncillaryRoleEnum] = Field(None, description="Identifies a party via its ancillary role on a transaction (e.g. CCP or DCO through which the trade should be cleared.)")
  """
  Identifies a party via its ancillary role on a transaction (e.g. CCP or DCO through which the trade should be cleared.)
  """
  legalEntity: Optional[LegalEntity] = Field(None, description="")
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('ancillaryParty', 'legalEntity', necessity=True)

from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum
from cdm.base.staticdata.party.LegalEntity import LegalEntity

AncillaryEntity.update_forward_refs()
