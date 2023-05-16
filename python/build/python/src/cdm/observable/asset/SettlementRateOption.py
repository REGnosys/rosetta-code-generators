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

__all__ = ['SettlementRateOption']


class SettlementRateOption(BaseDataClass):
  """
  Defines the settlement rate option to use for fixing in case of cash settlement. Currently only applicable to foreign exchange fixing in case of cross-currency settlement.
  """
  priceSourceDisruption: Optional[PriceSourceDisruption] = Field(None, description="An attribute defining the parameters to get a new quote when a settlement rate option is disrupted.")
  """
  An attribute defining the parameters to get a new quote when a settlement rate option is disrupted.
  """
  settlementRateOption: AttributeWithMeta[SettlementRateOptionEnum] | SettlementRateOptionEnum = Field(..., description="The rate source for the conversion to the settlement currency. This source is specified through a scheme that reflects the terms of the Annex A to the 1998 FX and Currency Option Definitions.")
  """
  The rate source for the conversion to the settlement currency. This source is specified through a scheme that reflects the terms of the Annex A to the 1998 FX and Currency Option Definitions.
  """

from cdm.observable.asset.PriceSourceDisruption import PriceSourceDisruption
from cdm.observable.asset.SettlementRateOptionEnum import SettlementRateOptionEnum

SettlementRateOption.update_forward_refs()
