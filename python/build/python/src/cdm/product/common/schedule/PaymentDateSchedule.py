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

__all__ = ['PaymentDateSchedule']


class PaymentDateSchedule(BaseDataClass):
  """
  The payment dates when specified as relative to a set of dates specified somewhere else in the instance document/transaction, e.g. the valuation dates as typically the case for equity swaps, or when specified as a calculation period schedule.
  """
  finalPaymentDate: Optional[AdjustableOrRelativeDate] = Field(None, description="The last payment when specified as an adjustable or relative date, as in the FpML total return construct.")
  """
  The last payment when specified as an adjustable or relative date, as in the FpML total return construct.
  """
  interimPaymentDates: List[AdjustableRelativeOrPeriodicDates] = Field([], description="")

from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.base.datetime.AdjustableRelativeOrPeriodicDates import AdjustableRelativeOrPeriodicDates

PaymentDateSchedule.update_forward_refs()
