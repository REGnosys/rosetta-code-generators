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

__all__ = ['AdditionalObligations']


class AdditionalObligations(BaseDataClass):
  """
  The election of party specific additional obligations applicable to the agreement.
  """
  additionalObligations: str = Field(..., description="The party specific additional obligations applicable to the agreement.")
  """
  The party specific additional obligations applicable to the agreement.
  """
  party: CounterpartyRoleEnum = Field(..., description="The party that the additional obligations apply to.")
  """
  The party that the additional obligations apply to.
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

AdditionalObligations.update_forward_refs()
