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

__all__ = ['ListingType']


class ListingType(BaseDataClass):
  """
  Specifies a filter based on an underlying corporate financial official listing defined at a stock exchange.
  """
  exchange: Optional[AttributeWithMeta[str] | str] = Field(None, description="Represents a filter based on the Primary Stock Exchange facilitating the listing of companies, exchange of Stocks, Exchange traded Derivatives, Bonds, and other Securities expressed in ISO standard 10383.")
  """
  Represents a filter based on the Primary Stock Exchange facilitating the listing of companies, exchange of Stocks, Exchange traded Derivatives, Bonds, and other Securities expressed in ISO standard 10383.
  """
  index: Optional[Index] = Field(None, description="Represents a filter based on an index that measures a stock market, or a subset of a stock market.")
  """
  Represents a filter based on an index that measures a stock market, or a subset of a stock market.
  """
  sector: Optional[AttributeWithMeta[str] | str] = Field(None, description="Represents a filter based on an industry sector defined under a system for classifying industry types such as ‘Global Industry Classification Standard (GICS)’ and ‘North American Industry Classification System (NAICS)’")
  """
  Represents a filter based on an industry sector defined under a system for classifying industry types such as ‘Global Industry Classification Standard (GICS)’ and ‘North American Industry Classification System (NAICS)’
  """

from cdm.base.staticdata.asset.common.Index import Index

ListingType.update_forward_refs()
