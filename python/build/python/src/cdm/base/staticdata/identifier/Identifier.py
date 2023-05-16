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

__all__ = ['Identifier']


class Identifier(BaseDataClass):
  """
  A class to specify a generic identifier, applicable to CDM artefacts such as executions, contracts, lifecycle events and legal documents. An issuer can be associated with the actual identifier value as a way to properly qualify it.
  """
  assignedIdentifier: List[AssignedIdentifier] = Field([], description="The identifier value. This level of indirection between the issuer and the identifier and its version provides the ability to associate multiple identifiers to one issuer, consistently with the FpML PartyTradeIdentifier.")
  """
  The identifier value. This level of indirection between the issuer and the identifier and its version provides the ability to associate multiple identifiers to one issuer, consistently with the FpML PartyTradeIdentifier.
  """
  @rosetta_condition
  def cardinality_assignedIdentifier(self):
    return check_cardinality(self.assignedIdentifier, 1, None)
  
  issuer: Optional[AttributeWithMeta[str] | str] = Field(None, description="The identifier issuer, when specified explicitly alongside the identifier value (instead of being specified by reference to a party).")
  """
  The identifier issuer, when specified explicitly alongside the identifier value (instead of being specified by reference to a party).
  """
  issuerReference: Optional[AttributeWithReference | Party] = Field(None, description="The identifier issuer, when specified by reference to a party specified as part of the transaction.")
  """
  The identifier issuer, when specified by reference to a party specified as part of the transaction.
  """
  
  @rosetta_condition
  def condition_0_IssuerChoice(self):
    """
    The identifier issuer is specified either explicitly or by reference to one of the parties.
    """
    return self.check_one_of_constraint('issuerReference', 'issuer', necessity=True)

from cdm.base.staticdata.identifier.AssignedIdentifier import AssignedIdentifier
from cdm.base.staticdata.party.Party import Party

Identifier.update_forward_refs()
