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

__all__ = ['FloatingRateSpecification']

from cdm.product.asset.FloatingRate import FloatingRate

class FloatingRateSpecification(FloatingRate):
  """
  A class to specify the floating interest rate by extending the floating rate definition with a set of attributes that specify such rate: the initial value specified as part of the trade, the rounding convention, the averaging method and the negative interest rate treatment.
  """
  averagingMethod: Optional[AveragingWeightingMethodEnum] = Field(None, description="If averaging is applicable, this component specifies whether a weighted or unweighted average method of calculation is to be used. The component must only be included when averaging applies.")
  """
  If averaging is applicable, this component specifies whether a weighted or unweighted average method of calculation is to be used. The component must only be included when averaging applies.
  """
  finalRateRounding: Optional[Rounding] = Field(None, description="The rounding convention to apply to the final rate used in determination of a calculation period amount.")
  """
  The rounding convention to apply to the final rate used in determination of a calculation period amount.
  """
  initialRate: Optional[Price] = Field(None, description="The initial floating rate reset agreed between the principal parties involved in the trade. This is assumed to be the first required reset rate for the first regular calculation period. It should only be included when the rate is not equal to the rate published on the source implied by the floating rate index. An initial rate of 5% would be represented as 0.05.")
  """
  The initial floating rate reset agreed between the principal parties involved in the trade. This is assumed to be the first required reset rate for the first regular calculation period. It should only be included when the rate is not equal to the rate published on the source implied by the floating rate index. An initial rate of 5% would be represented as 0.05.
  """
  negativeInterestRateTreatment: Optional[NegativeInterestRateTreatmentEnum] = Field(None, description="The specification of any provisions for calculating payment obligations when a floating rate is negative (either due to a quoted negative floating rate or by operation of a spread that is subtracted from the floating rate).")
  """
  The specification of any provisions for calculating payment obligations when a floating rate is negative (either due to a quoted negative floating rate or by operation of a spread that is subtracted from the floating rate).
  """

from cdm.base.math.AveragingWeightingMethodEnum import AveragingWeightingMethodEnum
from cdm.base.math.Rounding import Rounding
from cdm.observable.asset.Price import Price
from cdm.product.asset.NegativeInterestRateTreatmentEnum import NegativeInterestRateTreatmentEnum

FloatingRateSpecification.update_forward_refs()
