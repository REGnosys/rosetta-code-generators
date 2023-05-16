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

__all__ = ['SecurityProviderRightsEventElection']


class SecurityProviderRightsEventElection(BaseDataClass):
  """
  A class to specify party specific Secured Party Rights Event language.
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  rightsEvent: bool = Field(..., description="")

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

SecurityProviderRightsEventElection.update_forward_refs()
