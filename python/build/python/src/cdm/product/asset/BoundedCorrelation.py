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

__all__ = ['BoundedCorrelation']


class BoundedCorrelation(BaseDataClass):
  """
  Describes correlation bounds, which form a cap and a floor on the realized correlation.
  """
  maximumBoundaryPercent: Optional[Decimal] = Field(None, description="Maximum Boundary as a percentage of the Strike Price.")
  """
  Maximum Boundary as a percentage of the Strike Price.
  """
  minimumBoundaryPercent: Optional[Decimal] = Field(None, description="Minimum Boundary as a percentage of the Strike Price.")
  """
  Minimum Boundary as a percentage of the Strike Price.
  """


BoundedCorrelation.update_forward_refs()
