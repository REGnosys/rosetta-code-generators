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

__all__ = ['StrikeSchedule']

from cdm.product.common.schedule.RateSchedule import RateSchedule

class StrikeSchedule(RateSchedule):
  """
  A class describing a schedule of cap or floor rates.
  """
  buyer: Optional[PayerReceiverEnum] = Field(None, description="The buyer of the option.")
  """
  The buyer of the option.
  """
  seller: Optional[PayerReceiverEnum] = Field(None, description="The party that has sold.")
  """
  The party that has sold.
  """

from cdm.base.staticdata.party.PayerReceiverEnum import PayerReceiverEnum

StrikeSchedule.update_forward_refs()
