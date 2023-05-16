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

__all__ = ['IdentifiedProduct']


class IdentifiedProduct(BaseDataClass):
  """
  An abstract class to specify a product which terms are abstracted through reference data.
  """
  productIdentifier: ProductIdentifier = Field(..., description="")

from cdm.base.staticdata.asset.common.ProductIdentifier import ProductIdentifier

IdentifiedProduct.update_forward_refs()
