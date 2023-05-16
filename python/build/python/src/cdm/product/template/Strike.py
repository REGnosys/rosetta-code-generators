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

__all__ = ['Strike']


class Strike(BaseDataClass):
  """
  A class describing a single cap or floor rate.
  """
  buyer: Optional[PayerReceiverEnum] = Field(None, description="The buyer of the option.")
  """
  The buyer of the option.
  """
  seller: Optional[PayerReceiverEnum] = Field(None, description="The party that has sold.")
  """
  The party that has sold.
  """
  strikeRate: Decimal = Field(..., description="The rate for a cap or floor.")
  """
  The rate for a cap or floor.
  """

from cdm.base.staticdata.party.PayerReceiverEnum import PayerReceiverEnum

Strike.update_forward_refs()
