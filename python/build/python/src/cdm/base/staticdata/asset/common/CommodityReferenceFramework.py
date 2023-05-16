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

__all__ = ['CommodityReferenceFramework']


class CommodityReferenceFramework(BaseDataClass):
  """
  Specifies the type of commodity.
  """
  capacityUnit: Optional[CapacityUnitEnum] = Field(None, description="Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.")
  """
  Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.
  """
  commodityBase: AttributeWithMeta[str] | str = Field(..., description="Identifies the base type of the commodity being traded, using the names defined in the ISDA 2005 Commodity Definitions SubAnnex A where possible, e.g. AgriculturalProducts, CommodityCompositeIndices, Energy, Freight, Metals, or PaperAndPlastic. Implementors can define their own scheme with additional values.")
  """
  Identifies the base type of the commodity being traded, using the names defined in the ISDA 2005 Commodity Definitions SubAnnex A where possible, e.g. AgriculturalProducts, CommodityCompositeIndices, Energy, Freight, Metals, or PaperAndPlastic. Implementors can define their own scheme with additional values.
  """
  commodityName: str = Field(..., description="Identifies the commodity more specifically. Where possible, this should follow the naming convention used in the 2005 ISDA Commodity Definitions SubAnnex A, including the subCommodity and additional qualifiers, but should be limited to 256 characters or less.")
  """
  Identifies the commodity more specifically. Where possible, this should follow the naming convention used in the 2005 ISDA Commodity Definitions SubAnnex A, including the subCommodity and additional qualifiers, but should be limited to 256 characters or less.
  """
  currency: AttributeWithMeta[str] | str = Field(..., description="Defines the currency in which the commodity is priced.")
  """
  Defines the currency in which the commodity is priced.
  """
  subCommodity: AttributeWithMeta[str] | str = Field(..., description="Identifies the sub product type of the commodity being traded, using the names defined in the ISDA 2005 Commodity Definitions SubAnnex A where possible, e.g. under Energy, the possible values are Benzene, Coal, DieselFuel, Electricity, FuelOil, GasOil, Gasoline, HeatingOil, JetFuelKerosene, Methanol, Naphtha, NaturalGas, NaturalGasLiquids, Oil, and UltraLowSulpherDiesel. Implementors can define their own scheme with additional values.")
  """
  Identifies the sub product type of the commodity being traded, using the names defined in the ISDA 2005 Commodity Definitions SubAnnex A where possible, e.g. under Energy, the possible values are Benzene, Coal, DieselFuel, Electricity, FuelOil, GasOil, Gasoline, HeatingOil, JetFuelKerosene, Methanol, Naphtha, NaturalGas, NaturalGasLiquids, Oil, and UltraLowSulpherDiesel. Implementors can define their own scheme with additional values.
  """
  weatherUnit: Optional[WeatherUnitEnum] = Field(None, description="Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.")
  """
  Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.
  """
  
  @rosetta_condition
  def condition_0_CommodityReferenceFrameworkChoice(self):
    """
    Requires that either the capacity unit or weather unit is populated.
    """
    return self.check_one_of_constraint('capacityUnit', 'weatherUnit', necessity=False)

from cdm.base.math.CapacityUnitEnum import CapacityUnitEnum
from cdm.base.math.WeatherUnitEnum import WeatherUnitEnum

CommodityReferenceFramework.update_forward_refs()
