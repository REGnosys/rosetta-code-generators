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

__all__ = ['IssuerCriteria']


class IssuerCriteria(BaseDataClass):
  """
  Represents a criteria used to specify eligible collateral issuers.
  """
  counterpartyOwnIssuePermitted: Optional[bool] = Field(None, description="Represents a filter based on whether it is permitted for the underlying asset to be issued by the posting entity or part of their corporate family.")
  """
  Represents a filter based on whether it is permitted for the underlying asset to be issued by the posting entity or part of their corporate family.
  """
  issuerAgencyRating: List[AgencyRatingCriteria] = Field([], description="Represents an agency rating based on default risk and creditors claim in event of default associated with asset issuer.")
  """
  Represents an agency rating based on default risk and creditors claim in event of default associated with asset issuer.
  """
  issuerCountryOfOrigin: List[AttributeWithMeta[str] | str] = Field([], description="Represents a filter based on the issuing entity country of origin, which is the same as filtering by eligible Sovereigns.")
  """
  Represents a filter based on the issuing entity country of origin, which is the same as filtering by eligible Sovereigns.
  """
  issuerName: List[LegalEntity] = Field([], description="Specifies the issuing entity name or LEI.")
  """
  Specifies the issuing entity name or LEI.
  """
  issuerType: List[CollateralIssuerType] = Field([], description="Represents a filter based on the type of entity issuing the asset.")
  """
  Represents a filter based on the type of entity issuing the asset.
  """
  sovereignAgencyRating: List[AgencyRatingCriteria] = Field([], description="Represents an agency rating based on default risk of the country of the issuer.")
  """
  Represents an agency rating based on default risk of the country of the issuer.
  """

from cdm.legaldocumentation.csa.AgencyRatingCriteria import AgencyRatingCriteria
from cdm.base.staticdata.party.LegalEntity import LegalEntity
from cdm.base.staticdata.asset.common.CollateralIssuerType import CollateralIssuerType

IssuerCriteria.update_forward_refs()
