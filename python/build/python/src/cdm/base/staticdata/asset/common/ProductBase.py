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

__all__ = ['ProductBase']


class ProductBase(BaseDataClass):
  """
  Serves as an abstract class to specify a product using a productIdentifier.
  """
  productIdentifier: List[AttributeWithAddress[ProductIdentifier] | ProductIdentifier] = Field([], description="Comprises an identifier and a source. The associated metadata key denotes the ability to associate a hash value to the ProductIdentifier instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.")
  """
  Comprises an identifier and a source. The associated metadata key denotes the ability to associate a hash value to the ProductIdentifier instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.
  """
  productTaxonomy: List[ProductTaxonomy] = Field([], description="Specifies the product taxonomy, which is composed of a taxonomy value and a taxonomy source.")
  """
  Specifies the product taxonomy, which is composed of a taxonomy value and a taxonomy source.
  """

from cdm.base.staticdata.asset.common.ProductIdentifier import ProductIdentifier
from cdm.base.staticdata.asset.common.ProductTaxonomy import ProductTaxonomy

ProductBase.update_forward_refs()
