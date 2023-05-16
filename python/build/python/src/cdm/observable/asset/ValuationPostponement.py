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

__all__ = ['ValuationPostponement']


class ValuationPostponement(BaseDataClass):
  """
  Specifies how long to wait to get a quote from a settlement rate option upon a price source disruption.
  """
  maximumDaysOfPostponement: int = Field(..., description="The maximum number of days to wait for a quote from the disrupted settlement rate option before proceeding to the next method.")
  """
  The maximum number of days to wait for a quote from the disrupted settlement rate option before proceeding to the next method.
  """


ValuationPostponement.update_forward_refs()
