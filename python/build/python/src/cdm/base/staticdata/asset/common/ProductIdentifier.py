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

__all__ = ['ProductIdentifier']


class ProductIdentifier(BaseDataClass):
  """
  Comprises an identifier and a source. The associated metadata key denotes the ability to associate a hash value to the ProductIdentifier instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.
  """
  identifier: AttributeWithMeta[str] | str = Field(..., description="Provides an identifier associated with a specific product.  The identifier is unique within the public source specified in the source attribute.")
  """
  Provides an identifier associated with a specific product.  The identifier is unique within the public source specified in the source attribute.
  """
  source: ProductIdTypeEnum = Field(..., description="Defines the source of the identifier.")
  """
  Defines the source of the identifier.
  """

from cdm.base.staticdata.asset.common.ProductIdTypeEnum import ProductIdTypeEnum

ProductIdentifier.update_forward_refs()
