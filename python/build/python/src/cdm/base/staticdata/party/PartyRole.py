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

__all__ = ['PartyRole']


class PartyRole(BaseDataClass):
  """
  A class to specify the role(s) that party(ies) may have in relation to the execution, contract or other legal agreement.
  """
  ownershipPartyReference: Optional[AttributeWithReference | Party] = Field(None, description="A reference to the party that has ownership of this party role information. FpML specifies that For shared trade information, this attribute will reference the originator of the data (for example, an execution facility or clearing house).")
  """
  A reference to the party that has ownership of this party role information. FpML specifies that For shared trade information, this attribute will reference the originator of the data (for example, an execution facility or clearing house).
  """
  partyReference: AttributeWithReference | Party = Field(..., description="A reference to the party to which the role refers to.")
  """
  A reference to the party to which the role refers to.
  """
  role: PartyRoleEnum = Field(..., description="The party role.")
  """
  The party role.
  """

from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.PartyRoleEnum import PartyRoleEnum

PartyRole.update_forward_refs()
