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

__all__ = ['TelephoneNumber']


class TelephoneNumber(BaseDataClass):
  """
  A class to specify a telephone number as a type of phone number (e.g. work, personal, ...) alongside with the actual number.
  """
  number: str = Field(..., description="The actual telephone number.")
  """
  The actual telephone number.
  """
  telephoneNumberType: Optional[TelephoneTypeEnum] = Field(None, description="The type of telephone number, e.g. work, mobile.")
  """
  The type of telephone number, e.g. work, mobile.
  """

from cdm.base.staticdata.party.TelephoneTypeEnum import TelephoneTypeEnum

TelephoneNumber.update_forward_refs()
