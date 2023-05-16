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

__all__ = ['GracePeriodExtension']


class GracePeriodExtension(BaseDataClass):
  applicable: bool = Field(..., description="Indicates whether the grace period extension provision is applicable.")
  """
  Indicates whether the grace period extension provision is applicable.
  """
  gracePeriod: Optional[Offset] = Field(None, description="The number of calendar or business days after any due date that the reference entity has to fulfil its obligations before a failure to pay credit event is deemed to have occurred. ISDA 2003 Term: Grace Period.")
  """
  The number of calendar or business days after any due date that the reference entity has to fulfil its obligations before a failure to pay credit event is deemed to have occurred. ISDA 2003 Term: Grace Period.
  """

from cdm.base.datetime.Offset import Offset

GracePeriodExtension.update_forward_refs()
