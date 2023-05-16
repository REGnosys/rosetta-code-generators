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

__all__ = ['ProductTaxonomy']


class ProductTaxonomy(BaseDataClass):
  """
  Specifies the product taxonomy, which is composed of a taxonomy value and a taxonomy source.
  """
  primaryAssetClass: Optional[AttributeWithMeta[AssetClassEnum] | AssetClassEnum] = Field(None, description="Classifies the most important risk class of the trade.")
  """
  Classifies the most important risk class of the trade.
  """
  productQualifier: Optional[str] = Field(None, description="Derived from the product payout features using a CDM product qualification function that determines the product type based on the product payout features.")
  """
  Derived from the product payout features using a CDM product qualification function that determines the product type based on the product payout features.
  """
  secondaryAssetClass: List[AttributeWithMeta[AssetClassEnum] | AssetClassEnum] = Field([], description=" Classifies additional risk classes of the trade, if any.")
  """
   Classifies additional risk classes of the trade, if any.
  """
  taxonomySource: Optional[TaxonomySourceEnum] = Field(None, description="Specifies the taxonomy source.")
  """
  Specifies the taxonomy source.
  """
  taxonomyValue: Optional[AttributeWithMeta[str] | str] = Field(None, description="Specifies the taxonomy value.")
  """
  Specifies the taxonomy value.
  """
  
  @rosetta_condition
  def condition_0_TaxonomyValue(self):
    """
    Requires a taxonomy value to be chosen.
    """
    return self.check_one_of_constraint('taxonomyValue', 'productQualifier', 'primaryAssetClass', 'secondaryAssetClass', necessity=True)
  
  @rosetta_condition
  def condition_1_TaxonomySource(self):
    """
    A taxonomy source can only be associated with a taxonomyValue or productQualifier
    """
    def _then_fn0():
      return (((self.taxonomyValue) is not None) or ((self.productQualifier) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.taxonomySource) is not None), _then_fn0, _else_fn0)

from cdm.base.staticdata.asset.common.AssetClassEnum import AssetClassEnum
from cdm.base.staticdata.asset.common.TaxonomySourceEnum import TaxonomySourceEnum

ProductTaxonomy.update_forward_refs()
