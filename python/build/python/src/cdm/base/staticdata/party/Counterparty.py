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

__all__ = ['Counterparty']


class Counterparty(BaseDataClass):
  """
  Defines a counterparty enumerated value, e.g. Party1 or Party2, with an associated party reference. The product is agnostic to the actual parties to the transaction, with the party references abstracted away from the product definition and replaced by the CounterpartyEnum (e.g. values Party1 or Party2). The CounterpartyEnum can then be positioned in the product (e.g. to specify which counterparty is the payer, receiver etc) and this Counterparty type, which is positioned outside of the product definition, allows the CounterpartyEnum to be associated with an actual party reference.
  """
  partyReference: AttributeWithReference | Party = Field(..., description="Specifies the party that is associated to the counterparty.")
  """
  Specifies the party that is associated to the counterparty.
  """
  role: CounterpartyRoleEnum = Field(..., description="Specifies the CounterpartyEnum, e.g. either Party1 or Party2, that is associated to the partyReference.")
  """
  Specifies the CounterpartyEnum, e.g. either Party1 or Party2, that is associated to the partyReference.
  """

from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

Counterparty.update_forward_refs()
