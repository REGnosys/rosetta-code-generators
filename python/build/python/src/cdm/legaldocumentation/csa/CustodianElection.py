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

__all__ = ['CustodianElection']


class CustodianElection(BaseDataClass):
  """
  A class to specify the custodian and custody account details for each party to the agreement.
  """
  custodian: Optional[LegalEntity] = Field(None, description="The custody agent. While ISDA Create only specifies the custodian's name, specifying the legal entity as part of the CDM is deemed more appropriate, while this will still provide the ability to accommodate situations where only the entity name is available, as the entityId attribute is optional as part of the LegalEntity class.")
  """
  The custody agent. While ISDA Create only specifies the custodian's name, specifying the legal entity as part of the CDM is deemed more appropriate, while this will still provide the ability to accommodate situations where only the entity name is available, as the entityId attribute is optional as part of the LegalEntity class.
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  segregatedCashAccount: Optional[Account] = Field(None, description="The identification of the segregated cash account for the purpose of holding cash collateral.")
  """
  The identification of the segregated cash account for the purpose of holding cash collateral.
  """
  segregatedSecurityAccount: Optional[Account] = Field(None, description="The identification of the segregated security account for the purpose of holding security collateral.")
  """
  The identification of the segregated security account for the purpose of holding security collateral.
  """

from cdm.base.staticdata.party.LegalEntity import LegalEntity
from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum
from cdm.base.staticdata.party.Account import Account

CustodianElection.update_forward_refs()
