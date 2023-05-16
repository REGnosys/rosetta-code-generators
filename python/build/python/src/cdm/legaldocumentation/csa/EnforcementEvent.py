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

__all__ = ['EnforcementEvent']


class EnforcementEvent(BaseDataClass):
  """
  A class to specify Enforcement Events specific to Security Agreements
  """
  earlyTerminationDate: bool = Field(..., description="The early termination election")
  """
  The early termination election
  """
  failureToPay: Optional[bool] = Field(None, description="The failure to pay election")
  """
  The failure to pay election
  """


EnforcementEvent.update_forward_refs()
