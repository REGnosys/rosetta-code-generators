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

__all__ = ['CreditLimitInformation']


class CreditLimitInformation(BaseDataClass):
  """
  A class to represent the credit limit utilisation information.
  """
  limitApplicable: List[LimitApplicableExtended] = Field([], description="")
  @rosetta_condition
  def cardinality_limitApplicable(self):
    return check_cardinality(self.limitApplicable, 1, None)
  

from cdm.event.workflow.LimitApplicableExtended import LimitApplicableExtended

CreditLimitInformation.update_forward_refs()
