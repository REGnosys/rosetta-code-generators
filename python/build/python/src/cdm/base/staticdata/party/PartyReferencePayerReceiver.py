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

__all__ = ['PartyReferencePayerReceiver']


class PartyReferencePayerReceiver(BaseDataClass):
  """
  Specifies the parties responsible for making and receiving payments defined by this structure.
  """
  payerAccountReference: Optional[AttributeWithReference | Account] = Field(None, description="A reference to the account responsible for making the payments defined by this structure.")
  """
  A reference to the account responsible for making the payments defined by this structure.
  """
  payerPartyReference: AttributeWithReference | Party = Field(..., description="The party responsible for making the payments defined by this structure.")
  """
  The party responsible for making the payments defined by this structure.
  """
  receiverAccountReference: Optional[AttributeWithReference | Account] = Field(None, description="A reference to the account that receives the payments corresponding to this structure.")
  """
  A reference to the account that receives the payments corresponding to this structure.
  """
  receiverPartyReference: AttributeWithReference | Party = Field(..., description="The party that receives the payments corresponding to this structure.")
  """
  The party that receives the payments corresponding to this structure.
  """

from cdm.base.staticdata.party.Account import Account
from cdm.base.staticdata.party.Party import Party

PartyReferencePayerReceiver.update_forward_refs()
