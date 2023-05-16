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

__all__ = ['RelatedParty']


class RelatedParty(BaseDataClass):
  accountReference: Optional[AttributeWithReference | Account] = Field(None, description="Reference to an account.")
  """
  Reference to an account.
  """
  partyReference: AttributeWithReference | Party = Field(..., description="Reference to a party.")
  """
  Reference to a party.
  """
  role: PartyRoleEnum = Field(..., description="The category of the relationship. The related party performs the role specified in this field for the base party. For example, if the role is ,Guarantor, the related party acts as a guarantor for the base party.")
  """
  The category of the relationship. The related party performs the role specified in this field for the base party. For example, if the role is ,Guarantor, the related party acts as a guarantor for the base party.
  """

from cdm.base.staticdata.party.Account import Account
from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.PartyRoleEnum import PartyRoleEnum

RelatedParty.update_forward_refs()
