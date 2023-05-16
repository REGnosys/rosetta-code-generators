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

__all__ = ['InterestAdjustmentPeriodicity']


class InterestAdjustmentPeriodicity(BaseDataClass):
  """
  A class to specify the Interest Adjustment periodicity either through a standardized election or a custom one. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).
  """
  customElection: Optional[str] = Field(None, description="The Interest Adjustment periodicity when specified through a custom election.")
  """
  The Interest Adjustment periodicity when specified through a custom election.
  """
  standardElection: Optional[InterestAdjustmentPeriodicityEnum] = Field(None, description="The Interest Adjustment periodicity when specified through a standardized election.")
  """
  The Interest Adjustment periodicity when specified through a standardized election.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('standardElection', 'customElection', necessity=True)

from cdm.legaldocumentation.csa.InterestAdjustmentPeriodicityEnum import InterestAdjustmentPeriodicityEnum

InterestAdjustmentPeriodicity.update_forward_refs()
