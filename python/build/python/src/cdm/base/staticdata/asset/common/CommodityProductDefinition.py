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

__all__ = ['CommodityProductDefinition']


class CommodityProductDefinition(BaseDataClass):
  """
  Specifies the commodity underlier in the event that no ISDA Commodity Reference Price exists.
  """
  exchangeId: AttributeWithMeta[str] | str = Field(..., description=" Identifies the exchange from which the reference price should be sourced, using the scheme at the following url: http://www.fpml.org/coding-scheme/external/exchange-id-MIC-1-0")
  """
   Identifies the exchange from which the reference price should be sourced, using the scheme at the following url: http://www.fpml.org/coding-scheme/external/exchange-id-MIC-1-0
  """
  priceSource: Optional[PriceSource] = Field(None, description="Specifies a publication that provides the commodity price, including, where applicable the details of where in the publication the price is published.  Applicable when the commodity reference price is not a futures contract")
  """
  Specifies a publication that provides the commodity price, including, where applicable the details of where in the publication the price is published.  Applicable when the commodity reference price is not a futures contract
  """
  referenceFramework: CommodityReferenceFramework = Field(..., description="Specifies the type of commodity.")
  """
  Specifies the type of commodity.
  """
  
  @rosetta_condition
  def condition_0_CommodityProductDefinitionChoice(self):
    """
    Requires the definition of either delivery date parameters or non-exchange price source.
    """
    return self.check_one_of_constraint('exchangeId', 'priceSource', necessity=False)

from cdm.base.staticdata.asset.common.PriceSource import PriceSource
from cdm.base.staticdata.asset.common.CommodityReferenceFramework import CommodityReferenceFramework

CommodityProductDefinition.update_forward_refs()
