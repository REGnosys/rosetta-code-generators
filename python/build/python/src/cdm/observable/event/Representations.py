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

__all__ = ['Representations']


class Representations(BaseDataClass):
  additionalAcknowledgements: Optional[bool] = Field(None, description="If true, then additional acknowledgements are applicable.")
  """
  If true, then additional acknowledgements are applicable.
  """
  agreementsRegardingHedging: bool = Field(..., description="If true, then agreements regarding hedging are applicable.")
  """
  If true, then agreements regarding hedging are applicable.
  """
  indexDisclaimer: Optional[bool] = Field(None, description="If present and true, then index disclaimer is applicable.")
  """
  If present and true, then index disclaimer is applicable.
  """
  nonReliance: bool = Field(..., description="If true, then non reliance is applicable.")
  """
  If true, then non reliance is applicable.
  """


Representations.update_forward_refs()
