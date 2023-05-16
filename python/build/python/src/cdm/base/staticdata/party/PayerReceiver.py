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

__all__ = ['PayerReceiver']


class PayerReceiver(BaseDataClass):
  """
  Specifies the parties responsible for making and receiving payments defined by this structure.
  """
  payer: CounterpartyRoleEnum = Field(..., description="Specifies the counterparty responsible for making the payments defined by this structure.  The party is one of the two principal parties to the transaction.")
  """
  Specifies the counterparty responsible for making the payments defined by this structure.  The party is one of the two principal parties to the transaction.
  """
  receiver: CounterpartyRoleEnum = Field(..., description="Specifies the party that receives the payments corresponding to this structure.  The party is one of the two counterparties to the transaction.")
  """
  Specifies the party that receives the payments corresponding to this structure.  The party is one of the two counterparties to the transaction.
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

PayerReceiver.update_forward_refs()
