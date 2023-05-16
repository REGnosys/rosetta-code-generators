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

__all__ = ['BillingRecordInstruction']


class BillingRecordInstruction(BaseDataClass):
  """
  Specifies the instructions for creation of a billing record.
  """
  observation: List[Observation] = Field([], description="The observations used to calculate the billing amount.")
  """
  The observations used to calculate the billing amount.
  """
  @rosetta_condition
  def cardinality_observation(self):
    return check_cardinality(self.observation, 1, None)
  
  recordEndDate: date = Field(..., description="The ending date of the period described by this record")
  """
  The ending date of the period described by this record
  """
  recordStartDate: date = Field(..., description="The starting date of the period described by this record")
  """
  The starting date of the period described by this record
  """
  settlementDate: date = Field(..., description="The date for settlement of the transfer.")
  """
  The date for settlement of the transfer.
  """
  tradeState: AttributeWithReference | TradeState = Field(..., description="The trade for the individual billing record.")
  """
  The trade for the individual billing record.
  """

from cdm.observable.event.Observation import Observation
from cdm.event.common.TradeState import TradeState

BillingRecordInstruction.update_forward_refs()
