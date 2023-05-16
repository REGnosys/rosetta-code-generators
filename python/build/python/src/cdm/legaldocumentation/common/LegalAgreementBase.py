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

__all__ = ['LegalAgreementBase']


class LegalAgreementBase(BaseDataClass):
  """
  Specifies the legal agreement baseline information, being negotiated or having been executed. It excludes specialized elections
  """
  agreementDate: Optional[date] = Field(None, description="The date on which the legal agreement has been agreed between the parties. This corresponds to the Date of Deed in an English Law document.")
  """
  The date on which the legal agreement has been agreed between the parties. This corresponds to the Date of Deed in an English Law document.
  """
  attachment: List[Resource] = Field([], description="A human readable document, for example a confirmation.")
  """
  A human readable document, for example a confirmation.
  """
  contractualParty: List[AttributeWithReference | Party] = Field([], description="The two contractual parties to the legal agreement, which reference information is positioned as part of the partyInformation attribute.")
  """
  The two contractual parties to the legal agreement, which reference information is positioned as part of the partyInformation attribute.
  """
  @rosetta_condition
  def cardinality_contractualParty(self):
    return check_cardinality(self.contractualParty, 2, 2)
  
  effectiveDate: Optional[date] = Field(None, description="The date on which, or as of which, the agreement is effective, if different from the agreement date. It is expected that it will most often correspond to the agreement date, although there could be situations where the parties will explicitly agree on a distinct effective date.")
  """
  The date on which, or as of which, the agreement is effective, if different from the agreement date. It is expected that it will most often correspond to the agreement date, although there could be situations where the parties will explicitly agree on a distinct effective date.
  """
  identifier: List[Identifier] = Field([], description="The legal agreement identifier. Several identifiers can be specified.")
  """
  The legal agreement identifier. Several identifiers can be specified.
  """
  legalAgreementIdentification: LegalAgreementIdentification = Field(..., description="The type of legal agreement, identified via a set of composable attributes: agreementName, publisher, governing law and version, e.g. ISDA 2013 Standard Credit Support Annex English Law.")
  """
  The type of legal agreement, identified via a set of composable attributes: agreementName, publisher, governing law and version, e.g. ISDA 2013 Standard Credit Support Annex English Law.
  """
  otherParty: List[PartyRole] = Field([], description="The role(s) that other party(ies) may have in relation to the legal agreement, further to the contractual parties.")
  """
  The role(s) that other party(ies) may have in relation to the legal agreement, further to the contractual parties.
  """

from cdm.legaldocumentation.common.Resource import Resource
from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.identifier.Identifier import Identifier
from cdm.legaldocumentation.common.LegalAgreementIdentification import LegalAgreementIdentification
from cdm.base.staticdata.party.PartyRole import PartyRole

LegalAgreementBase.update_forward_refs()
