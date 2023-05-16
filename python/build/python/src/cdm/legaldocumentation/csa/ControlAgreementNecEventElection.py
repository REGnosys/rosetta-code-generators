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

__all__ = ['ControlAgreementNecEventElection']


class ControlAgreementNecEventElection(BaseDataClass):
  """
  A class to specify party specific Control Agreement language related to delivery of a Notice of Exclusive Control
  """
  necEvent: bool = Field(..., description="")
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

ControlAgreementNecEventElection.update_forward_refs()
