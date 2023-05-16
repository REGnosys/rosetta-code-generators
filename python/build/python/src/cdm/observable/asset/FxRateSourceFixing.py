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

__all__ = ['FxRateSourceFixing']


class FxRateSourceFixing(BaseDataClass):
  """
  Describes a rate source to be fixed and the date the fixing occurs
  """
  fixingDate: AdjustableDate = Field(..., description="The date on which the fixing is scheduled to occur.")
  """
  The date on which the fixing is scheduled to occur.
  """
  settlementRateSource: FxSettlementRateSource = Field(..., description="")

from cdm.base.datetime.AdjustableDate import AdjustableDate
from cdm.observable.asset.FxSettlementRateSource import FxSettlementRateSource

FxRateSourceFixing.update_forward_refs()
