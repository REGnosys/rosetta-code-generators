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

__all__ = ['AncillaryParty']


class AncillaryParty(BaseDataClass):
  """
  Defines an ancillary role enumerated value with an associated party reference. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and this AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference.
  """
  onBehalfOf: Optional[CounterpartyRoleEnum] = Field(None, description="Optionally specifies the counterparty that the ancillary party is acting on behalf of.")
  """
  Optionally specifies the counterparty that the ancillary party is acting on behalf of.
  """
  partyReference: List[AttributeWithReference | Party] = Field([], description="Specifies the party, or parties, associated to the ancillary role.")
  """
  Specifies the party, or parties, associated to the ancillary role.
  """
  @rosetta_condition
  def cardinality_partyReference(self):
    return check_cardinality(self.partyReference, 1, None)
  
  role: AncillaryRoleEnum = Field(..., description="Specifies the AncillaryRoleEnum that is associated to the party reference. An ancillary party is any involved party that is not one of the two principal parties to the transaction.")
  """
  Specifies the AncillaryRoleEnum that is associated to the party reference. An ancillary party is any involved party that is not one of the two principal parties to the transaction.
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum
from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

AncillaryParty.update_forward_refs()
