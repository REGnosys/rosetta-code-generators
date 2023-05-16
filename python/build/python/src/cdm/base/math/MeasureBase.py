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

__all__ = ['MeasureBase']


class MeasureBase(BaseDataClass):
  """
  Provides an abstract type to define a measure as a number associated to a unit. This type is abstract because all its attributes are optional. The types that extend it can specify further existence constraints.
  """
  unit: Optional[UnitType] = Field(None, description="Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).")
  """
  Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).
  """
  value: Optional[Decimal] = Field(None, description="Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.")
  """
  Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.
  """

from cdm.base.math.UnitType import UnitType

MeasureBase.update_forward_refs()
