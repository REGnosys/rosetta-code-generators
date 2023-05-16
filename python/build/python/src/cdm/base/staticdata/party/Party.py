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

__all__ = ['Party']


class Party(BaseDataClass):
  """
  A class to specify a party, without a qualification as to whether this party is a legal entity or a natural person, although the model provides the ability to associate a person (or set of persons) to a party, which use case would imply that such party would be a legal entity (even if not formally specified as such). 
  """
  account: Optional[Account] = Field(None, description="The account that might be associated with the party. At most one account can be specified, as it is expected that this information is used in the context of a contract or legal document where only one account per party can be associated with such object.")
  """
  The account that might be associated with the party. At most one account can be specified, as it is expected that this information is used in the context of a contract or legal document where only one account per party can be associated with such object.
  """
  businessUnit: List[BusinessUnit] = Field([], description="Optional organization unit information used to describe the organization units (e.g. trading desks) involved in a transaction or business process, incl. the contact information (when relevant).")
  """
  Optional organization unit information used to describe the organization units (e.g. trading desks) involved in a transaction or business process, incl. the contact information (when relevant).
  """
  contactInformation: Optional[ContactInformation] = Field(None, description="The postal/street address, telephone number, email address and/or web page. If the contact information is specific to the associated business unit(s) or person (s), it should be associated with those.")
  """
  The postal/street address, telephone number, email address and/or web page. If the contact information is specific to the associated business unit(s) or person (s), it should be associated with those.
  """
  name: Optional[AttributeWithMeta[str] | str] = Field(None, description="The party name.")
  """
  The party name.
  """
  partyId: List[PartyIdentifier] = Field([], description="The identifier associated with a party, e.g. the 20 digits LEI code.")
  """
  The identifier associated with a party, e.g. the 20 digits LEI code.
  """
  @rosetta_condition
  def cardinality_partyId(self):
    return check_cardinality(self.partyId, 1, None)
  
  person: List[NaturalPerson] = Field([], description="The person(s) who might be associated with the party as part of the execution, contract or legal document.")
  """
  The person(s) who might be associated with the party as part of the execution, contract or legal document.
  """

from cdm.base.staticdata.party.Account import Account
from cdm.base.staticdata.party.BusinessUnit import BusinessUnit
from cdm.base.staticdata.party.ContactInformation import ContactInformation
from cdm.base.staticdata.party.PartyIdentifier import PartyIdentifier
from cdm.base.staticdata.party.NaturalPerson import NaturalPerson

Party.update_forward_refs()
