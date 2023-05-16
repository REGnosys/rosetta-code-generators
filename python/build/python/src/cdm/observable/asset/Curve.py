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

__all__ = ['Curve']


class Curve(BaseDataClass):
  commodityCurve: Optional[AttributeWithMeta[CommodityReferencePriceEnum] | CommodityReferencePriceEnum] = Field(None, description="")
  interestRateCurve: Optional[InterestRateCurve] = Field(None, description="")
  
  @rosetta_condition
  def condition_0_Curve(self):
    return self.check_one_of_constraint('interestRateCurve', 'commodityCurve', necessity=True)

from cdm.observable.asset.CommodityReferencePriceEnum import CommodityReferencePriceEnum
from cdm.observable.asset.InterestRateCurve import InterestRateCurve

Curve.update_forward_refs()
