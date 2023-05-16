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

__all__ = ['Account']


class Account(BaseDataClass):
  """
  A class to specify an account as an account number alongside, optionally. an account name, an account type, an account beneficiary and a servicing party.
  """
  accountBeneficiary: Optional[AttributeWithReference | Party] = Field(None, description="A reference to the party beneficiary of the account.")
  """
  A reference to the party beneficiary of the account.
  """
  accountName: Optional[AttributeWithMeta[str] | str] = Field(None, description="The name by which the account is known.")
  """
  The name by which the account is known.
  """
  accountNumber: AttributeWithMeta[str] | str = Field(..., description="The account number.")
  """
  The account number.
  """
  accountType: Optional[AttributeWithMeta[AccountTypeEnum] | AccountTypeEnum] = Field(None, description="The type of account, e.g. client, house.")
  """
  The type of account, e.g. client, house.
  """
  partyReference: Optional[AttributeWithReference | Party] = Field(None, description="A reference to the party to which the account refers to.")
  """
  A reference to the party to which the account refers to.
  """
  servicingParty: Optional[AttributeWithReference | Party] = Field(None, description="The reference to the legal entity that services the account, i.e. in the books of which the account is held.")
  """
  The reference to the legal entity that services the account, i.e. in the books of which the account is held.
  """

from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.AccountTypeEnum import AccountTypeEnum

Account.update_forward_refs()
