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

__all__ = ['DeterminationMethodology']


class DeterminationMethodology(BaseDataClass):
  """
  Specifies the method according to which an amount or a date is determined.
  """
  averagingMethod: Optional[AveragingCalculationMethodEnum] = Field(None, description="Specifies enumerations for the type of averaging calculation.")
  """
  Specifies enumerations for the type of averaging calculation.
  """
  determinationMethod: Optional[DeterminationMethodEnum] = Field(None, description="Represents a more granular dimention of observation. Typically relevent for resolving a unique equity price, which can be expressed as trade-weighted or volume-weighted averages.")
  """
  Represents a more granular dimention of observation. Typically relevent for resolving a unique equity price, which can be expressed as trade-weighted or volume-weighted averages.
  """

from cdm.base.math.AveragingCalculationMethodEnum import AveragingCalculationMethodEnum
from cdm.observable.common.DeterminationMethodEnum import DeterminationMethodEnum

DeterminationMethodology.update_forward_refs()
