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

__all__ = ['UnitType']


class UnitType(BaseDataClass):
  """
  Defines the unit to be used for price, quantity, or other purposes
  """
  capacityUnit: Optional[CapacityUnitEnum] = Field(None, description="Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.")
  """
  Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.
  """
  currency: Optional[AttributeWithMeta[str] | str] = Field(None, description="Defines the currency to be used as a unit for a price, quantity, or other purpose.")
  """
  Defines the currency to be used as a unit for a price, quantity, or other purpose.
  """
  financialUnit: Optional[FinancialUnitEnum] = Field(None, description="Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.")
  """
  Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.
  """
  weatherUnit: Optional[WeatherUnitEnum] = Field(None, description="Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.")
  """
  Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.
  """
  
  @rosetta_condition
  def condition_0_UnitType(self):
    """
    Requires that a unit type must be set.
    """
    return self.check_one_of_constraint('capacityUnit', 'weatherUnit', 'financialUnit', 'currency', necessity=True)

from cdm.base.math.CapacityUnitEnum import CapacityUnitEnum
from cdm.base.math.FinancialUnitEnum import FinancialUnitEnum
from cdm.base.math.WeatherUnitEnum import WeatherUnitEnum

UnitType.update_forward_refs()
