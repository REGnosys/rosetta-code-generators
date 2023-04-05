""" Basic maths concepts: quantity and unit, rounding, curve / schedule,
    non-negativity constraint etc
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case4, the example reflects the first 3 data types from
# base-math-types.rosetta
from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, root_validator
from cdm import check_one_of_constraint
from cdm.base.datetime import Frequency
from .base_math_enum import CapacityUnitEnum
from .base_math_enum import WeatherUnitEnum
from .base_math_enum import FinancialUnitEnum

__all__ = ['UnitType']


class UnitType(BaseModel):
    """ Defines the unit to be used for price, quantity, or other purposes
    """
    capacityUnit: Optional[CapacityUnitEnum] = Field(
        None,
        description='Provides an enumerated value for a capacity unit, '
                    'generally used in the context of defining quantities for '
                    'commodities.'
    )
    """ Provides an enumerated value for a capacity unit, generally used in the
        context of defining quantities for commodities.
    """
    weatherUnit: Optional[WeatherUnitEnum] = Field(
        None,
        description='Provides an enumerated values for a weather unit, '
                    'generally used in the context of defining quantities'
    )
    """ Provides an enumerated values for a weather unit, generally used in the
        context of defining quantities
    """
    financialUnit: Optional[FinancialUnitEnum] = Field(
        None,
        description='Provides an enumerated value for financial units, '
                    'generally used in the context of defining quantities for '
                    'securities.'
    )
    """ Provides an enumerated value for financial units, generally used in the
        context of defining quantities for securities.
    """
    currency: Optional[str] = Field(
        None,
        description='Defines the currency to be used as a unit for a price, '
                    'quantity, or other purpose.'
    )
    """ Defines the currency to be used as a unit for a price, quantity, or
        other purpose.
    """
    frequency: Optional[Frequency] = Field(
        None,
        description='Defines the frequency to be used as a unit for a price, '
                    'quantity, or other purpose.'
    )
    """ Defines the frequency to be used as a unit for a price, quantity, or
        other purpose.
    """

    @root_validator
    @classmethod
    def condition_0_UnitType(cls, values):
        """ Requires that a unit type must be set. """
        return check_one_of_constraint(values, 'capacityUnit', 'weatherUnit',
                                       'financialUnit', 'currency')

# EOF
