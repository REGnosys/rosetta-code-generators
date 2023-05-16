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

__all__ = ['InterestShortFall']


class InterestShortFall(BaseDataClass):
  """
  A class to specify the interest shortfall floating rate payment event.
  """
  compounding: bool = Field(..., description="")
  interestShortfallCap: InterestShortfallCapEnum = Field(..., description="Specifies the nature of the interest Shortfall cap (i.e. Fixed Cap or Variable Cap) in the case where it is applicable. ISDA 2003 Term: Interest Shortfall Cap.")
  """
  Specifies the nature of the interest Shortfall cap (i.e. Fixed Cap or Variable Cap) in the case where it is applicable. ISDA 2003 Term: Interest Shortfall Cap.
  """
  rateSource: Optional[AttributeWithMeta[FloatingRateIndexEnum] | FloatingRateIndexEnum] = Field(None, description="The rate source in the case of a variable cap.")
  """
  The rate source in the case of a variable cap.
  """

from cdm.product.asset.InterestShortfallCapEnum import InterestShortfallCapEnum
from cdm.base.staticdata.asset.rates.FloatingRateIndexEnum import FloatingRateIndexEnum

InterestShortFall.update_forward_refs()
