""" Basic maths concepts: quantity and unit, rounding, curve / schedule,
    non-negativity constraint etc
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case4, the example reflects the first 3 data types from
# base-math-types.rosetta
from __future__ import annotations
from typing import Optional
from pydantic import Field
from cdm.utils import *
from cdm.base.math.CapacityUnitEnum import CapacityUnitEnum
from cdm.base.math.WeatherUnitEnum import WeatherUnitEnum
from cdm.base.math.FinancialUnitEnum import FinancialUnitEnum

__all__ = ['UnitType']


class UnitType(BaseDataClass):
    """
    Defines the unit to be used for price, quantity, or other purposes
    """
    capacityUnit: Optional[CapacityUnitEnum] = Field(None, description="Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.")
    """
    Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.
    """
    currency: Optional[str] = Field(None, description="Defines the currency to be used as a unit for a price, quantity, or other purpose.")
    """
    Defines the currency to be used as a unit for a price, quantity, or other purpose.
    """
    financialUnit: Optional[FinancialUnitEnum] = Field(None, description="Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.")
    """
    Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.
    """
    frequency: Optional[Frequency] = Field(None, description="Defines the frequency to be used as a unit for a price, quantity, or other purpose.")
    """
    Defines the frequency to be used as a unit for a price, quantity, or other purpose.
    """
    weatherUnit: Optional[WeatherUnitEnum] = Field(None, description="Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.")
    """
    Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.
    """

    @cdm_condition
    def condition_0_UnitType(self):
        """
        Requires that a unit type must be set.
        """
        return self.check_one_of_constraint('capacityUnit', 'weatherUnit', 'financialUnit', 'currency', necessity=True)


from cdm.base.datetime.Frequency import Frequency

UnitType.update_forward_refs()

# EOF
