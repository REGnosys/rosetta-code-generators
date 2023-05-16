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

__all__ = ['AddressForNotices']


class AddressForNotices(BaseDataClass):
  """
  Specification of the address and other details for notices.
  """
  additionalNotices: List[PartyContactInformation] = Field([], description="The optional specification of additional information when a party requires notices to be delivered to more than one address.")
  """
  The optional specification of additional information when a party requires notices to be delivered to more than one address.
  """
  primaryNotices: ContactElection = Field(..., description="Specification of primary notice details")
  """
  Specification of primary notice details
  """

from cdm.base.staticdata.party.PartyContactInformation import PartyContactInformation
from cdm.legaldocumentation.csa.ContactElection import ContactElection

AddressForNotices.update_forward_refs()
