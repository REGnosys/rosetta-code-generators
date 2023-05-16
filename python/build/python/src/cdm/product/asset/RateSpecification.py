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

__all__ = ['RateSpecification']


class RateSpecification(BaseDataClass):
  """
   A class to specify the fixed interest rate, floating interest rate or inflation rate.
  """
  fixedRate: Optional[FixedRateSpecification] = Field(None, description="The fixed rate or fixed rate specification expressed as explicit fixed rates and dates.")
  """
  The fixed rate or fixed rate specification expressed as explicit fixed rates and dates.
  """
  floatingRate: Optional[FloatingRateSpecification] = Field(None, description="The floating interest rate specification, which includes the definition of the floating rate index. the tenor, the initial value, and, when applicable, the spread, the rounding convention, the averaging method and the negative interest rate treatment.")
  """
  The floating interest rate specification, which includes the definition of the floating rate index. the tenor, the initial value, and, when applicable, the spread, the rounding convention, the averaging method and the negative interest rate treatment.
  """
  inflationRate: Optional[InflationRateSpecification] = Field(None, description="An inflation rate calculation definition.")
  """
  An inflation rate calculation definition.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('fixedRate', 'floatingRate', 'inflationRate', necessity=True)

from cdm.product.asset.FixedRateSpecification import FixedRateSpecification
from cdm.product.asset.FloatingRateSpecification import FloatingRateSpecification
from cdm.product.asset.InflationRateSpecification import InflationRateSpecification

RateSpecification.update_forward_refs()
