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

__all__ = ['QuantitySchedule']

from cdm.base.math.MeasureSchedule import MeasureSchedule

class QuantitySchedule(MeasureSchedule):
  """
  Specifies a quantity schedule to be associated to a financial product to represent a trade amount. This data type extends MeasureSchedule with several unit or multiplier attributes that are used to define financial quantities. This data type is generically based on a schedule and can also be used to represent a quantity as a single value.
  """
  frequency: Optional[Frequency] = Field(None, description="Defines the frequency to be used when defining a quantity. For example a quantity may be specified as a number of barrels of oil per day, which needs multiplying by the number of days in the relevant period to get the total quantity as a number of barrels.")
  """
  Defines the frequency to be used when defining a quantity. For example a quantity may be specified as a number of barrels of oil per day, which needs multiplying by the number of days in the relevant period to get the total quantity as a number of barrels.
  """
  multiplier: Optional[Measure] = Field(None, description="Defines an optional number that the quantity should be multiplied by to derive a total quantity. This number is associated to a unit. For example in the case of the Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Contract on the CME, where the unit would be contracts, the multiplier value would 1,000 and the mulitiplier unit would be 1,000 MT (Metric Tons).")
  """
  Defines an optional number that the quantity should be multiplied by to derive a total quantity. This number is associated to a unit. For example in the case of the Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Contract on the CME, where the unit would be contracts, the multiplier value would 1,000 and the mulitiplier unit would be 1,000 MT (Metric Tons).
  """
  
  @rosetta_condition
  def condition_0_Quantity_multiplier(self):
    """
    Requires that the multiplier must be positive.
    """
    def _then_fn0():
      return all_elements(self.multiplier.value, ">=", 0.0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.multiplier) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_UnitOfAmountExists(self):
    """
    Requires that a unit of amount must be specified for any quantity.
    """
    return ((self.unit) is not None)

from cdm.base.datetime.Frequency import Frequency
from cdm.base.math.Measure import Measure

QuantitySchedule.update_forward_refs()
