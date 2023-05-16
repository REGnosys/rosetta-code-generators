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

__all__ = ['AggregationParameters']


class AggregationParameters(BaseDataClass):
  """
   Parameters to be used to filter events that are relevant to a given portfolio in order to calculate the state of this portfolio. The attributes correspond to all the possible aggregation criteria that can be used and these criteria can be combined. All the attributes are optional.
  """
  dateTime: datetime = Field(..., description="To aggregate as of a particular date")
  """
  To aggregate as of a particular date
  """
  party: List[AttributeWithReference | Party] = Field([], description="To aggregate based on a selection of party(ies) / legal entity(ies).")
  """
  To aggregate based on a selection of party(ies) / legal entity(ies).
  """
  positionStatus: Optional[PositionStatusEnum] = Field(None, description="To aggregate based on position status (EXECUTED, SETTLED etc)")
  """
  To aggregate based on position status (EXECUTED, SETTLED etc)
  """
  product: List[Product] = Field([], description="To aggregate based on a selection of products.")
  """
  To aggregate based on a selection of products.
  """
  productQualifier: List[str] = Field([], description="To aggregate based on a selection of product type(s).")
  """
  To aggregate based on a selection of product type(s).
  """
  totalPosition: Optional[bool] = Field(None, description="Specifies whether to calculate total position to given date, or only daily position for the given date.")
  """
  Specifies whether to calculate total position to given date, or only daily position for the given date.
  """
  tradeReference: List[AttributeWithReference | Trade] = Field([], description="")

from cdm.base.staticdata.party.Party import Party
from cdm.event.position.PositionStatusEnum import PositionStatusEnum
from cdm.product.template.Product import Product
from cdm.event.common.Trade import Trade

AggregationParameters.update_forward_refs()
