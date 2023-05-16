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

__all__ = ['AveragingCalculation']


class AveragingCalculation(BaseDataClass):
  """
  Defines parameters for use in cases when a valuation or other term is based on an average of market observations.
  """
  averagingMethod: AveragingCalculationMethod = Field(..., description="Specifies enumerations for the type of averaging calculation.")
  """
  Specifies enumerations for the type of averaging calculation.
  """
  precision: Rounding = Field(..., description="Rounding applied to the average calculation. ")
  """
  Rounding applied to the average calculation. 
  """

from cdm.base.math.AveragingCalculationMethod import AveragingCalculationMethod
from cdm.base.math.Rounding import Rounding

AveragingCalculation.update_forward_refs()
