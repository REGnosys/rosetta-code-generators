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

__all__ = ['CollateralProvisions']


class CollateralProvisions(BaseDataClass):
  """
  Contains collateral attributes which can also inherit information from a master agreement.
  """
  collateralType: CollateralTypeEnum = Field(..., description="Cash or NonCash collateral")
  """
  Cash or NonCash collateral
  """
  eligibleCollateral: List[EligibleCollateralSchedule] = Field([], description="The eligible collateral as specified in relation to the transaction.")
  """
  The eligible collateral as specified in relation to the transaction.
  """
  marginPercentage: Optional[CollateralValuationTreatment] = Field(None, description="Specification of the valuation treatment for the specified collateral.")
  """
  Specification of the valuation treatment for the specified collateral.
  """

from cdm.product.template.CollateralTypeEnum import CollateralTypeEnum
from cdm.legaldocumentation.csa.EligibleCollateralSchedule import EligibleCollateralSchedule
from cdm.legaldocumentation.csa.CollateralValuationTreatment import CollateralValuationTreatment

CollateralProvisions.update_forward_refs()
