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

__all__ = ['AdjustableRelativeOrPeriodicDates']


class AdjustableRelativeOrPeriodicDates(BaseDataClass):
    """
    A class giving the choice between defining a series of dates as an explicit list of dates together with applicable adjustments or as relative to some other series of (anchor) dates, or as a calculation period schedule.
    """
    adjustableDates: Optional[AdjustableDates] = Field(None, description="A series of dates that shall be subject to adjustment if they would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date.")
    """
    A series of dates that shall be subject to adjustment if they would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date.
    """
    periodicDates: Optional[PeriodicDates] = Field(None, description="A calculation period schedule.")
    """
    A calculation period schedule.
    """
    relativeDates: Optional[RelativeDates] = Field(None, description="A series of dates specified as some offset to another series of dates (the anchor dates).")
    """
    A series of dates specified as some offset to another series of dates (the anchor dates).
    """
    
    @rosetta_condition
    def condition_0_AdjustableRelativeOrPeriodicDatesChoice(self):
        """
        Choice rule to represent an FpML choice construct.
        """
        return self.check_one_of_constraint('adjustableDates', 'relativeDates', 'periodicDates', necessity=True)

from cdm.base.datetime.AdjustableDates import AdjustableDates
from cdm.base.datetime.PeriodicDates import PeriodicDates
from cdm.base.datetime.RelativeDates import RelativeDates

AdjustableRelativeOrPeriodicDates.update_forward_refs()
