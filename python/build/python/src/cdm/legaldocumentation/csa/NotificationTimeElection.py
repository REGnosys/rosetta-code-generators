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

__all__ = ['NotificationTimeElection']


class NotificationTimeElection(BaseDataClass):
  """
  A class to specify the notification time election by the respective parties to the agreement. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (d)(iii): Notification Time. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (e)(iii): Notification Time. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(iii): Notification Time.
  """
  customNotification: Optional[str] = Field(None, description="The Notification Time as a custom election.")
  """
  The Notification Time as a custom election.
  """
  notificationTime: Optional[BusinessCenterTime] = Field(None, description="The Notification Time as a time that is qualified as a standard business center.")
  """
  The Notification Time as a time that is qualified as a standard business center.
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  
  @rosetta_condition
  def condition_0_NotificationTimeElectionChoice(self):
    """
    The Notification Time is specified either as a time that is qualified by a standard business center or as a custom election.
    """
    return self.check_one_of_constraint('notificationTime', 'customNotification', necessity=True)

from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime
from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

NotificationTimeElection.update_forward_refs()
