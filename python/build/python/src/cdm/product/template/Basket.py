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

__all__ = ['Basket']

from cdm.base.staticdata.asset.common.ProductBase import ProductBase

class Basket(ProductBase):
  """
  Defines a custom basket by referencing a product identifier and its consituents.
  """
  basketConstituent: List[Product] = Field([], description="Identifies the constituents of the basket")
  """
  Identifies the constituents of the basket
  """
  @rosetta_condition
  def cardinality_basketConstituent(self):
    return check_cardinality(self.basketConstituent, 1, None)
  

from cdm.product.template.Product import Product

Basket.update_forward_refs()
