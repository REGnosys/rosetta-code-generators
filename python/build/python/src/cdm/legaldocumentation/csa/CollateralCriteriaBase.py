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

__all__ = ['CollateralCriteriaBase']


class CollateralCriteriaBase(BaseDataClass):
  """
  Represents a set of criteria used to specify and desribe collateral.
  """
  asset: List[AssetCriteria] = Field([], description="Represents a filter based on the criteria realted to the asset.")
  """
  Represents a filter based on the criteria realted to the asset.
  """
  issuer: List[IssuerCriteria] = Field([], description="Represents a filter based criterai related to the issuer.")
  """
  Represents a filter based criterai related to the issuer.
  """

from cdm.legaldocumentation.csa.AssetCriteria import AssetCriteria
from cdm.legaldocumentation.csa.IssuerCriteria import IssuerCriteria

CollateralCriteriaBase.update_forward_refs()
