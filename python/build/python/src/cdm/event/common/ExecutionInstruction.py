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

__all__ = ['ExecutionInstruction']


class ExecutionInstruction(BaseDataClass):
  """
  Specifies instructions for execution of a transaction, consisting of a product, price, quantity, parties, trade identifier, execution details, and settlement terms.
  """
  ancillaryParty: List[AncillaryParty] = Field([], description="Maps any ancillary parties, e.g. parties involved in the transaction that are not one of the two principal parties.")
  """
  Maps any ancillary parties, e.g. parties involved in the transaction that are not one of the two principal parties.
  """
  collateral: Optional[Collateral] = Field(None, description="Detail the collateral requirement anticipated with the transaction.")
  """
  Detail the collateral requirement anticipated with the transaction.
  """
  counterparty: List[Counterparty] = Field([], description="Maps two defined parties to counterparty enums for the transacted product.")
  """
  Maps two defined parties to counterparty enums for the transacted product.
  """
  @rosetta_condition
  def cardinality_counterparty(self):
    return check_cardinality(self.counterparty, 2, 2)
  
  executionDetails: ExecutionDetails = Field(..., description="Specifies the type and venue of execution, e.g. via voice, or electronically.")
  """
  Specifies the type and venue of execution, e.g. via voice, or electronically.
  """
  parties: List[Party] = Field([], description="Defines all parties to that execution, including agents and brokers.")
  """
  Defines all parties to that execution, including agents and brokers.
  """
  @rosetta_condition
  def cardinality_parties(self):
    return check_cardinality(self.parties, 2, None)
  
  partyRoles: List[PartyRole] = Field([], description="Defines the role(s) that party(ies) may have in relation to the execution.")
  """
  Defines the role(s) that party(ies) may have in relation to the execution.
  """
  priceQuantity: List[PriceQuantity] = Field([], description="Defines the prices (e.g. spread, equity price, FX rate), quantities (e.g. currency amount, no. shares) and settlement terms (e.g. initial fee, broker fee, up-front cds payment or option premium settlement) associated with the constituents of the transacted product.")
  """
  Defines the prices (e.g. spread, equity price, FX rate), quantities (e.g. currency amount, no. shares) and settlement terms (e.g. initial fee, broker fee, up-front cds payment or option premium settlement) associated with the constituents of the transacted product.
  """
  @rosetta_condition
  def cardinality_priceQuantity(self):
    return check_cardinality(self.priceQuantity, 1, None)
  
  product: Product = Field(..., description="Defines the financial product to be executed and contract formed.")
  """
  Defines the financial product to be executed and contract formed.
  """
  tradeDate: AttributeWithMeta[date] | date = Field(..., description="Denotes the trade/execution date.")
  """
  Denotes the trade/execution date.
  """
  tradeIdentifier: List[Identifier] = Field([], description="Denotes one or more identifiers associated with the transaction.")
  """
  Denotes one or more identifiers associated with the transaction.
  """
  @rosetta_condition
  def cardinality_tradeIdentifier(self):
    return check_cardinality(self.tradeIdentifier, 1, None)
  

from cdm.base.staticdata.party.AncillaryParty import AncillaryParty
from cdm.legaldocumentation.csa.Collateral import Collateral
from cdm.base.staticdata.party.Counterparty import Counterparty
from cdm.event.common.ExecutionDetails import ExecutionDetails
from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.PartyRole import PartyRole
from cdm.product.common.settlement.PriceQuantity import PriceQuantity
from cdm.product.template.Product import Product
from cdm.base.staticdata.identifier.Identifier import Identifier

ExecutionInstruction.update_forward_refs()
