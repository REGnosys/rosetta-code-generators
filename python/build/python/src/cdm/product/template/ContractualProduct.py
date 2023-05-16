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

__all__ = ['ContractualProduct']

from cdm.base.staticdata.asset.common.ProductBase import ProductBase

class ContractualProduct(ProductBase):
  """
   A class to specify the contractual products' economic terms, alongside their product identification and product taxonomy. The contractual product class is meant to be used across the pre-execution, execution and (as part of the Contract) post-execution lifecycle contexts.
  """
  economicTerms: EconomicTerms = Field(..., description="The economic terms associated with a contractual product, i.e. the set of features that are price-forming.")
  """
  The economic terms associated with a contractual product, i.e. the set of features that are price-forming.
  """
  
  @rosetta_condition
  def condition_0_PrimaryAssetClass(self):
    """
    Specifies that when nonStandardisedTerms are True that a primary asset class must be specified.
    """
    def _then_fn0():
      return ((self.productTaxonomy.primaryAssetClass) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.economicTerms.nonStandardisedTerms, "=", False), _then_fn0, _else_fn0)

from cdm.product.template.EconomicTerms import EconomicTerms

ContractualProduct.update_forward_refs()
