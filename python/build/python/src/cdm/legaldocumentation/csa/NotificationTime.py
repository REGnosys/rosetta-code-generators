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

__all__ = ['NotificationTime']


class NotificationTime(BaseDataClass):
  """
  A class to specify the time by which a demand for the Transfer of Eligible Credit Support (IM) or Posted Credit Support (IM) needs to be made in order for the transfer to take place in accordance with the Transfer Timing provisions. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (d)(iii): Notification Time. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (e)(iii): Notification Time. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(iii): Notification Time.
  """
  disputeNotificationReference: Optional[bool] = Field(None, description="The determination of whether reference is made to dispute resolution notification timing in the agreement.")
  """
  The determination of whether reference is made to dispute resolution notification timing in the agreement.
  """
  partyElections: List[NotificationTimeElection] = Field([], description="The parties' Notification Time election.")
  """
  The parties' Notification Time election.
  """
  @rosetta_condition
  def cardinality_partyElections(self):
    return check_cardinality(self.partyElections, 2, 2)
  
  transferTimingProviso: Optional[bool] = Field(None, description="The determination of whether transfer timing language is applicable or not.")
  """
  The determination of whether transfer timing language is applicable or not.
  """

from cdm.legaldocumentation.csa.NotificationTimeElection import NotificationTimeElection

NotificationTime.update_forward_refs()
