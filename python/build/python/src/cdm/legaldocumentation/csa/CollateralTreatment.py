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

__all__ = ['CollateralTreatment']


class CollateralTreatment(BaseDataClass):
  """
  Specifies the treatment terms for the eligible collateral criteria specified.
  """
  concentrationLimit: List[ConcentrationLimit] = Field([], description="Specification of concentration limits applicable to the collateral criteria.")
  """
  Specification of concentration limits applicable to the collateral criteria.
  """
  isIncluded: bool = Field(..., description="A boolean attribute to specify whether collateral critieria are inclusion (True) or exclusion (False) criteria.")
  """
  A boolean attribute to specify whether collateral critieria are inclusion (True) or exclusion (False) criteria.
  """
  valuationTreatment: Optional[CollateralValuationTreatment] = Field(None, description="Specification of the valuation treatment for the specified collateral.")
  """
  Specification of the valuation treatment for the specified collateral.
  """

from cdm.legaldocumentation.csa.ConcentrationLimit import ConcentrationLimit
from cdm.legaldocumentation.csa.CollateralValuationTreatment import CollateralValuationTreatment

CollateralTreatment.update_forward_refs()
