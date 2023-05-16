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

__all__ = ['EvergreenProvision']


class EvergreenProvision(BaseDataClass):
  """
  Specifies a transaction which automatically extends for a specified timeframe until the exercise of an embedded option.
  """
  extensionFrequency: AdjustableRelativeOrPeriodicDates = Field(..., description="The frequency with which the evergreen contract will be extended if notice is not given.")
  """
  The frequency with which the evergreen contract will be extended if notice is not given.
  """
  finalPeriodFeeAdjustment: Optional[Price] = Field(None, description="An optional adjustment to the rate for the last period of the evergreen i.e. the period from when notice is given to stop rolling the contract through to the termination date.")
  """
  An optional adjustment to the rate for the last period of the evergreen i.e. the period from when notice is given to stop rolling the contract through to the termination date.
  """
  noticeDeadlineDateTime: Optional[datetime] = Field(None, description="A specific date and time for the notice deadline")
  """
  A specific date and time for the notice deadline
  """
  noticeDeadlinePeriod: Optional[RelativeDateOffset] = Field(None, description="Defines the minimum period before an evergreen is scheduled to terminate that notice can be given that it will terminate beyond the scheduled termination date.")
  """
  Defines the minimum period before an evergreen is scheduled to terminate that notice can be given that it will terminate beyond the scheduled termination date.
  """
  noticePeriod: RelativeDateOffset = Field(..., description="The length of each evergreen extension period relative to the effective date of the preceding contract.")
  """
  The length of each evergreen extension period relative to the effective date of the preceding contract.
  """
  singlePartyOption: Optional[PartyRole] = Field(None, description="If evergreen termination is not available to both parties then this component specifies the buyer and seller of the option.")
  """
  If evergreen termination is not available to both parties then this component specifies the buyer and seller of the option.
  """

from cdm.base.datetime.AdjustableRelativeOrPeriodicDates import AdjustableRelativeOrPeriodicDates
from cdm.observable.asset.Price import Price
from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset
from cdm.base.staticdata.party.PartyRole import PartyRole

EvergreenProvision.update_forward_refs()
