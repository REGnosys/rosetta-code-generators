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

__all__ = ['Affirmation']


class Affirmation(BaseDataClass):
  """
  A class to specify a trade affirmation.
  """
  identifier: List[Identifier] = Field([], description="The identifier(s) associated with the trade and resulting confirmation.")
  """
  The identifier(s) associated with the trade and resulting confirmation.
  """
  @rosetta_condition
  def cardinality_identifier(self):
    return check_cardinality(self.identifier, 1, None)
  
  lineage: Optional[Lineage] = Field(None, description="The lineage attribute provides a linkage to previous lifecycle events and associated data.")
  """
  The lineage attribute provides a linkage to previous lifecycle events and associated data.
  """
  party: List[Party] = Field([], description="The parties associated with the trade.")
  """
  The parties associated with the trade.
  """
  @rosetta_condition
  def cardinality_party(self):
    return check_cardinality(self.party, 1, None)
  
  partyRole: List[PartyRole] = Field([], description="The role(s) that party(ies) may have in relation to the trade")
  """
  The role(s) that party(ies) may have in relation to the trade
  """
  @rosetta_condition
  def cardinality_partyRole(self):
    return check_cardinality(self.partyRole, 1, None)
  
  status: AffirmationStatusEnum = Field(..., description="")
  
  @rosetta_condition
  def condition_0_BothBuyerAndSellerPartyRolesMustExist(self):
    """
    For an security affirmation, both buyer and seller party roles must exist.
    """
    def _then_fn0():
      return (contains(self.partyRole.role, PartyRoleEnum.BUYER) or contains(self.partyRole.role, PartyRoleEnum.SELLER))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.lineage.tradeReference.tradableProduct.product.security) is not None), _then_fn0, _else_fn0)

from cdm.base.staticdata.identifier.Identifier import Identifier
from cdm.event.common.Lineage import Lineage
from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.PartyRole import PartyRole
from cdm.event.common.AffirmationStatusEnum import AffirmationStatusEnum
from cdm.base.staticdata.party.PartyRoleEnum import PartyRoleEnum

Affirmation.update_forward_refs()
