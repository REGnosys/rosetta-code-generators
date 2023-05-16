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

__all__ = ['GeneralTerms']


class GeneralTerms(BaseDataClass):
  """
   A class specifying a set of non-monetary terms for the Credit Derivative Transaction, including the buyer and seller and selected items from the ISDA 2014 Credit Definition article II, such as the reference obligation and related terms. The CDM GeneralTerms class corresponds to the FpML GeneralTerms complex type, except that the effectiveDate and scheduledTerminationDate have been positioned as part of the InterestRatePayout class in the CDM instead of in GeneralTerms.
  """
  additionalTerm: List[AttributeWithMeta[str] | str] = Field([], description="This attribute is used for representing information contained in the Additional Terms field of the 2003 Master Credit Derivatives confirm.")
  """
  This attribute is used for representing information contained in the Additional Terms field of the 2003 Master Credit Derivatives confirm.
  """
  basketReferenceInformation: Optional[BasketReferenceInformation] = Field(None, description="This attribute contains all the terms relevant to defining the Credit Default Swap Basket.")
  """
  This attribute contains all the terms relevant to defining the Credit Default Swap Basket.
  """
  indexReferenceInformation: Optional[IndexReferenceInformation] = Field(None, description="This attribute contains all the terms relevant to defining the Credit DefaultSwap Index.")
  """
  This attribute contains all the terms relevant to defining the Credit DefaultSwap Index.
  """
  modifiedEquityDelivery: Optional[bool] = Field(None, description="Value of this attribute set to 'true' indicates that modified equity delivery is applicable.")
  """
  Value of this attribute set to 'true' indicates that modified equity delivery is applicable.
  """
  referenceInformation: Optional[ReferenceInformation] = Field(None, description="This attribute contains all the terms relevant to defining the reference entity and reference obligation(s).")
  """
  This attribute contains all the terms relevant to defining the reference entity and reference obligation(s).
  """
  substitution: Optional[bool] = Field(None, description="Value of this attribute set to 'true' indicates that substitution is applicable.")
  """
  Value of this attribute set to 'true' indicates that substitution is applicable.
  """
  
  @rosetta_condition
  def condition_0_GeneralTermsChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('referenceInformation', 'indexReferenceInformation', 'basketReferenceInformation', necessity=True)
  
  @rosetta_condition
  def condition_1_FpML_cd_41(self):
    """
    FpML validation rule cd-41 - If indexReferenceInformation/tranche does not exist, then modifiedEquityDelivery must not exist.
    """
    def _then_fn0():
      return ((self.modifiedEquityDelivery) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.indexReferenceInformation.tranche) is None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_FpML_cd_42(self):
    """
    FpML validation rule cd-42 - If basketReferenceInformation does not exist, then substitution must not exist.
    """
    def _then_fn0():
      return ((self.substitution) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.basketReferenceInformation) is None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_BasketReferenceInformationNameOrId(self):
    """
    The BasketReferenceInformation requires either a basket name or a basket identifier.
    """
    def _then_fn0():
      return (((self.basketReferenceInformation.basketName) is not None) or ((self.basketReferenceInformation.basketId) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.basketReferenceInformation) is not None), _then_fn0, _else_fn0)

from cdm.product.asset.BasketReferenceInformation import BasketReferenceInformation
from cdm.product.asset.IndexReferenceInformation import IndexReferenceInformation
from cdm.product.asset.ReferenceInformation import ReferenceInformation

GeneralTerms.update_forward_refs()
