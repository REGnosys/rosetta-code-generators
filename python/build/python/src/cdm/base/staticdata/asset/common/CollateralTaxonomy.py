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

__all__ = ['CollateralTaxonomy']


class CollateralTaxonomy(BaseDataClass):
  """
  Specifies the collateral taxonomy, which is composed of a taxonomy value and a taxonomy source.
  """
  taxonomySource: TaxonomySourceEnum = Field(..., description="Specifies the taxonomy source.")
  """
  Specifies the taxonomy source.
  """
  taxonomyValue: CollateralTaxonomyValue = Field(..., description="Specifies the taxonomy value.")
  """
  Specifies the taxonomy value.
  """
  
  @rosetta_condition
  def condition_0_Eu_EligibleCollateralTaxonomy(self):
    """
    If the Taxonomy Source is specified as EU EMIR Eligible Collateral then the enumeration must be EU EMIR Eligible Collateral.
    """
    def _then_fn0():
      return ((self.taxonomyValue.eu_EMIR_EligibleCollateral) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.taxonomySource, "=", TaxonomySourceEnum.EU_EMIR_ELIGIBLE_COLLATERAL_ASSET_CLASS), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_UkEligibleCollateralTaxonomy(self):
    """
    If the Taxonomy Source is specified as UK EMIR Eligible Collateral then the enumeration must be UK EMIR Eligible Collateral.
    """
    def _then_fn0():
      return ((self.taxonomyValue.uk_EMIR_EligibleCollateral) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.taxonomySource, "=", TaxonomySourceEnum.UK_EMIR_ELIGIBLE_COLLATERAL_ASSET_CLASS), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_UsEligibleCollateralTaxonomy(self):
    """
    If the Taxonomy Source is specified as US CFTCPR Eligbile Collateral then the enumeration must be US CFTCPR Eligible Collateral.
    """
    def _then_fn0():
      return ((self.taxonomyValue.us_CFTC_PR_EligibleCollateral) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.taxonomySource, "=", TaxonomySourceEnum.US_CFTC_PR_ELIGIBLE_COLLATERAL_ASSET_CLASS), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_TaxonomyValue(self):
    """
    If the Taxonomy Value is specified as a string then the taxonomy Source cannot be either EU Eligible Collateral or Uk Eligible Collateral or US Eligible Collateral.
    """
    def _then_fn0():
      return ((any_elements(self.taxonomySource, "<>", TaxonomySourceEnum.EU_EMIR_ELIGIBLE_COLLATERAL_ASSET_CLASS) and any_elements(self.taxonomySource, "<>", TaxonomySourceEnum.UK_EMIR_ELIGIBLE_COLLATERAL_ASSET_CLASS)) and any_elements(self.taxonomySource, "<>", TaxonomySourceEnum.US_CFTC_PR_ELIGIBLE_COLLATERAL_ASSET_CLASS))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.taxonomyValue.nonEnumeratedTaxonomyValue) is not None), _then_fn0, _else_fn0)

from cdm.base.staticdata.asset.common.TaxonomySourceEnum import TaxonomySourceEnum
from cdm.base.staticdata.asset.common.CollateralTaxonomyValue import CollateralTaxonomyValue

CollateralTaxonomy.update_forward_refs()
