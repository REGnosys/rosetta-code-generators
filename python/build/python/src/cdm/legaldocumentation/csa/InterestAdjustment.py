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

__all__ = ['InterestAdjustment']


class InterestAdjustment(BaseDataClass):
  """
  A class to specify whether the Interest Adjustment is applicable and what its periodicity is. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).
  """
  isApplicable: bool = Field(..., description="The Interest Adjustment is applicable when True and not applicable when False")
  """
  The Interest Adjustment is applicable when True and not applicable when False
  """
  periodicity: InterestAdjustmentPeriodicity = Field(..., description="The qualification of the Interest Adjustment periodicity.")
  """
  The qualification of the Interest Adjustment periodicity.
  """

from cdm.legaldocumentation.csa.InterestAdjustmentPeriodicity import InterestAdjustmentPeriodicity

InterestAdjustment.update_forward_refs()
