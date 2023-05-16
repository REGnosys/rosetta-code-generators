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

__all__ = ['PartyContactInformation']


class PartyContactInformation(BaseDataClass):
  """
  A class to specify contact information within a party: address and, optionally, associated business unit and person. This class also supports the ISDA CSA representation as a single string, through the address attribute.
  """
  additionalInformation: Optional[str] = Field(None, description="Specification of special instructions of the relevant party.")
  """
  Specification of special instructions of the relevant party.
  """
  businessUnit: List[BusinessUnit] = Field([], description="Optional organization unit information used to describe the organization units (e.g. trading desks) involved in a transaction or business process, incl. the contact information (when relevant).")
  """
  Optional organization unit information used to describe the organization units (e.g. trading desks) involved in a transaction or business process, incl. the contact information (when relevant).
  """
  contactInformation: Optional[ContactInformation] = Field(None, description="The postal/street address, telephone number, email address and/or web page. If the contact information is specific to the associated business unit(s), it should be associated with those.")
  """
  The postal/street address, telephone number, email address and/or web page. If the contact information is specific to the associated business unit(s), it should be associated with those.
  """
  partyReference: Optional[AttributeWithReference | Party] = Field(None, description="The reference to the party to which the contact information refers to.")
  """
  The reference to the party to which the contact information refers to.
  """
  person: List[NaturalPerson] = Field([], description="Optional information about people involved in a transaction or business process. (These are employees of the party.)")
  """
  Optional information about people involved in a transaction or business process. (These are employees of the party.)
  """

from cdm.base.staticdata.party.BusinessUnit import BusinessUnit
from cdm.base.staticdata.party.ContactInformation import ContactInformation
from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.NaturalPerson import NaturalPerson

PartyContactInformation.update_forward_refs()
