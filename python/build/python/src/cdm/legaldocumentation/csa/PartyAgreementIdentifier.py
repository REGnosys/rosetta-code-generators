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

__all__ = ['PartyAgreementIdentifier']


class PartyAgreementIdentifier(BaseDataClass):
  """
  A class defining a legal agreement identifier issued by the indicated party.
  """
  documentIdentifier: List[AttributeWithMeta[Identifier] | Identifier] = Field([], description="While FpML specifies the document identifier with a value and an associated scheme, the CDM makes use of the Identifier, which has an explicit issuer. The issuer of this identifier is not necessarily the same as the party reference.")
  """
  While FpML specifies the document identifier with a value and an associated scheme, the CDM makes use of the Identifier, which has an explicit issuer. The issuer of this identifier is not necessarily the same as the party reference.
  """
  @rosetta_condition
  def cardinality_documentIdentifier(self):
    return check_cardinality(self.documentIdentifier, 1, None)
  
  partyReference: AttributeWithReference | Party = Field(..., description="Party that issued the document identifier.")
  """
  Party that issued the document identifier.
  """

from cdm.base.staticdata.identifier.Identifier import Identifier
from cdm.base.staticdata.party.Party import Party

PartyAgreementIdentifier.update_forward_refs()
