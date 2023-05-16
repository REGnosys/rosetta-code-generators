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

__all__ = ['MakeWholeAmount']

from cdm.observable.asset.SwapCurveValuation import SwapCurveValuation

class MakeWholeAmount(SwapCurveValuation):
  """
  A class to specify the amount to be paid by the buyer of the option if the option is exercised prior to the Early Call Date (typically applicable to the convertible bond options).
  """
  earlyCallDate: AttributeWithMeta[date] | date = Field(..., description="Date prior to which the option buyer will have to pay a Make Whole Amount to the option seller if he/she exercises the option.")
  """
  Date prior to which the option buyer will have to pay a Make Whole Amount to the option seller if he/she exercises the option.
  """
  interpolationMethod: Optional[InterpolationMethodEnum] = Field(None, description="The type of interpolation method that the calculation agent reserves the right to use.")
  """
  The type of interpolation method that the calculation agent reserves the right to use.
  """

from cdm.observable.asset.InterpolationMethodEnum import InterpolationMethodEnum

MakeWholeAmount.update_forward_refs()
