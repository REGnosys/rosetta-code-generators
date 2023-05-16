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

__all__ = ['AdditionalRepresentationElection']


class AdditionalRepresentationElection(BaseDataClass):
  """
  A class to specify the parties' Additional Representation(s) election.
  """
  isApplicable: bool = Field(..., description="The Additional Representation is applicable when True, and not applicable when False.")
  """
  The Additional Representation is applicable when True, and not applicable when False.
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

AdditionalRepresentationElection.update_forward_refs()
