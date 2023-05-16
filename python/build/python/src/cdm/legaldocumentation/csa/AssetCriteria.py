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

__all__ = ['AssetCriteria']


class AssetCriteria(BaseDataClass):
  """
  Represents a set of criteria used to specify eligible collateral assets.
  """
  agencyRating: List[AgencyRatingCriteria] = Field([], description="Represents an agency rating based on default risk and creditors claim in event of default associated with specific instrument.")
  """
  Represents an agency rating based on default risk and creditors claim in event of default associated with specific instrument.
  """
  assetCountryOfOrigin: List[AttributeWithMeta[str] | str] = Field([], description="Represents a filter based on the asset country of origin.")
  """
  Represents a filter based on the asset country of origin.
  """
  collateralAssetType: List[AssetType] = Field([], description="Represents a filter based on the asset product type.")
  """
  Represents a filter based on the asset product type.
  """
  collateralTaxonomy: List[CollateralTaxonomy] = Field([], description="Specifies the collateral taxonomy,which is composed of a taxonomy value and a taxonomy source.")
  """
  Specifies the collateral taxonomy,which is composed of a taxonomy value and a taxonomy source.
  """
  denominatedCurrency: List[AttributeWithMeta[str] | str] = Field([], description="Represents a filter based on the underlying asset denominated currency.")
  """
  Represents a filter based on the underlying asset denominated currency.
  """
  domesticCurrencyIssued: Optional[bool] = Field(None, description="Identifies that the Security must be denominated in the domestic currency of the issuer.")
  """
  Identifies that the Security must be denominated in the domestic currency of the issuer.
  """
  listing: Optional[ListingType] = Field(None, description="Specifies the exchange, index or sector specific to listing of a security.")
  """
  Specifies the exchange, index or sector specific to listing of a security.
  """
  maturityRange: Optional[PeriodRange] = Field(None, description="Represents a filter based on the underlying asset maturity.")
  """
  Represents a filter based on the underlying asset maturity.
  """
  maturityType: Optional[MaturityTypeEnum] = Field(None, description="Specifies whether the maturity range is the remaining or original maturity.")
  """
  Specifies whether the maturity range is the remaining or original maturity.
  """
  productIdentifier: List[ProductIdentifier] = Field([], description="Represents a filter based on specific instrument identifiers (e.g. specific ISINs, CUSIPs etc).")
  """
  Represents a filter based on specific instrument identifiers (e.g. specific ISINs, CUSIPs etc).
  """
  
  @rosetta_condition
  def condition_0_AssetCriteriaChoice(self):
    """
    If any are specified, only one of AssetType, ProductTaxonomy or ProductIdentifer should exist.
    """
    return self.check_one_of_constraint('collateralAssetType', 'collateralTaxonomy', 'productIdentifier', necessity=False)

from cdm.legaldocumentation.csa.AgencyRatingCriteria import AgencyRatingCriteria
from cdm.base.staticdata.asset.common.AssetType import AssetType
from cdm.base.staticdata.asset.common.CollateralTaxonomy import CollateralTaxonomy
from cdm.legaldocumentation.csa.ListingType import ListingType
from cdm.base.datetime.PeriodRange import PeriodRange
from cdm.base.staticdata.asset.common.MaturityTypeEnum import MaturityTypeEnum
from cdm.base.staticdata.asset.common.ProductIdentifier import ProductIdentifier

AssetCriteria.update_forward_refs()
