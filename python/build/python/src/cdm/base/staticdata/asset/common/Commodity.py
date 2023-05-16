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

__all__ = ['Commodity']

from cdm.base.staticdata.asset.common.ProductBase import ProductBase

class Commodity(ProductBase):
  """
  Identifies a specific commodity by referencing a product identifier or by a product definition.
  """
  commodityProductDefinition: Optional[CommodityProductDefinition] = Field(None, description="Specifies the commodity underlier in the event that no ISDA Commodity Reference Benchmark exists.")
  """
  Specifies the commodity underlier in the event that no ISDA Commodity Reference Benchmark exists.
  """
  deliveryDateReference: Optional[DeliveryDateParameters] = Field(None, description="Specifies the parameters for identifying the relevant contract date when the commodity reference price is a futures contract.")
  """
  Specifies the parameters for identifying the relevant contract date when the commodity reference price is a futures contract.
  """
  description: Optional[str] = Field(None, description="Provides additional information about the commodity underlier.")
  """
  Provides additional information about the commodity underlier.
  """
  priceQuoteType: QuotationSideEnum = Field(..., description="Describes the required quote type of the underlying price that will be observed. Example values include 'Bid, 'Ask', 'Settlement' (for a futures contract) and 'WeightedAverage' (for some published prices and indices).")
  """
  Describes the required quote type of the underlying price that will be observed. Example values include 'Bid, 'Ask', 'Settlement' (for a futures contract) and 'WeightedAverage' (for some published prices and indices).
  """

from cdm.base.staticdata.asset.common.CommodityProductDefinition import CommodityProductDefinition
from cdm.base.staticdata.asset.common.DeliveryDateParameters import DeliveryDateParameters
from cdm.observable.asset.QuotationSideEnum import QuotationSideEnum

Commodity.update_forward_refs()
