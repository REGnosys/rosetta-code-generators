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

__all__ = ['AccessConditionsElections']


class AccessConditionsElections(BaseDataClass):
  """
  A class to specify the Termination Events that will be deemed an Access Condition (Initial Margin CSA) or a Specified Condition (Variation Margin CSA). ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (e)(ii). | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (f)(ii). | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (e)(ii). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (e): Conditions Precedent and Secured Party’s Rights and Remedies.
  """
  creditEventUponMerger: bool = Field(..., description="")
  forceMajeure: bool = Field(..., description="")
  illegality: bool = Field(..., description="")
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  taxEvent: bool = Field(..., description="")
  taxEventUponMerger: bool = Field(..., description="")

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

AccessConditionsElections.update_forward_refs()
