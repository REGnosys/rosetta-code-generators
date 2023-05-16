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

__all__ = ['CommodityPriceReturnTerms']


class CommodityPriceReturnTerms(BaseDataClass):
  """
  Defines parameters in which the commodity price is assessed.
  """
  conversionFactor: Optional[Decimal] = Field(None, description="Defines the conversion applied if the quantity unit on contract is different from unit on referenced underlier.")
  """
  Defines the conversion applied if the quantity unit on contract is different from unit on referenced underlier.
  """
  rollFeature: Optional[RollFeature] = Field(None, description="Used in conjunction with an exchange-based pricing source. Identifies a way in which the futures contracts referenced will roll between periods. ")
  """
  Used in conjunction with an exchange-based pricing source. Identifies a way in which the futures contracts referenced will roll between periods. 
  """
  rounding: Optional[Rounding] = Field(None, description="Defines rounding rules and precision to be used in the rounding of a number.")
  """
  Defines rounding rules and precision to be used in the rounding of a number.
  """
  spread: Optional[SpreadSchedule] = Field(None, description="Defines a spread value for one or more defined dates.")
  """
  Defines a spread value for one or more defined dates.
  """

from cdm.product.common.settlement.RollFeature import RollFeature
from cdm.base.math.Rounding import Rounding
from cdm.product.asset.SpreadSchedule import SpreadSchedule

CommodityPriceReturnTerms.update_forward_refs()
