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

__all__ = ['Lag']


class Lag(BaseDataClass):
  """
  The pricing period per calculation period if the pricing days do not wholly fall within the respective calculation period.
  """
  firstObservationDateOffset: Optional[Offset] = Field(None, description="Defines the offset of the series of pricing dates relative to the calculation period.")
  """
  Defines the offset of the series of pricing dates relative to the calculation period.
  """
  lagDuration: Offset = Field(..., description="Defines the offset of the series of pricing dates relative to the calculation period.")
  """
  Defines the offset of the series of pricing dates relative to the calculation period.
  """

from cdm.base.datetime.Offset import Offset

Lag.update_forward_refs()
