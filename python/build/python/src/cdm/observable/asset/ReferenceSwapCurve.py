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

__all__ = ['ReferenceSwapCurve']


class ReferenceSwapCurve(BaseDataClass):
  """
  A complex type used to specify the option and convertible bond option strike when expressed in reference to a swap curve.
  """
  makeWholeAmount: Optional[MakeWholeAmount] = Field(None, description="Amount to be paid by the buyer of the option if the option is exercised prior to the Early Call Date. (The market practice in the convertible bond option space being that the buyer should be penalised if he/she exercises the option early on.)")
  """
  Amount to be paid by the buyer of the option if the option is exercised prior to the Early Call Date. (The market practice in the convertible bond option space being that the buyer should be penalised if he/she exercises the option early on.)
  """
  swapUnwindValue: SwapCurveValuation = Field(..., description="")

from cdm.observable.asset.MakeWholeAmount import MakeWholeAmount
from cdm.observable.asset.SwapCurveValuation import SwapCurveValuation

ReferenceSwapCurve.update_forward_refs()
