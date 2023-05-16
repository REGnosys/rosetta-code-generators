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

__all__ = ['InflationRateSpecification']

from cdm.product.asset.FloatingRateSpecification import FloatingRateSpecification

class InflationRateSpecification(FloatingRateSpecification):
  """
  A data to:  specify the inflation rate.
  """
  fallbackBondApplicable: bool = Field(..., description="The applicability of a fallback bond as defined in the 2006 ISDA Inflation Derivatives Definitions, sections 1.3 and 1.8.")
  """
  The applicability of a fallback bond as defined in the 2006 ISDA Inflation Derivatives Definitions, sections 1.3 and 1.8.
  """
  indexSource: AttributeWithMeta[str] | str = Field(..., description="The reference source such as Reuters or Bloomberg. FpML specifies indexSource to be of type rateSourcePageScheme, but without specifying actual values.")
  """
  The reference source such as Reuters or Bloomberg. FpML specifies indexSource to be of type rateSourcePageScheme, but without specifying actual values.
  """
  inflationLag: Offset = Field(..., description="An off-setting period from the payment date which determines the reference period for which the inflation index is observed.")
  """
  An off-setting period from the payment date which determines the reference period for which the inflation index is observed.
  """
  initialIndexLevel: Optional[Decimal] = Field(None, description="Initial known index level for the first calculation period.")
  """
  Initial known index level for the first calculation period.
  """
  interpolationMethod: AttributeWithMeta[InterpolationMethodEnum] | InterpolationMethodEnum = Field(..., description="The method used when calculating the Inflation Index Level from multiple points. The most common is Linear.")
  """
  The method used when calculating the Inflation Index Level from multiple points. The most common is Linear.
  """
  mainPublication: AttributeWithMeta[str] | str = Field(..., description="The current main publication source such as relevant web site or a government body. FpML specifies mainPublication to be of type mainPublicationSource, but without specifying actual values.")
  """
  The current main publication source such as relevant web site or a government body. FpML specifies mainPublication to be of type mainPublicationSource, but without specifying actual values.
  """

from cdm.base.datetime.Offset import Offset
from cdm.observable.asset.InterpolationMethodEnum import InterpolationMethodEnum

InflationRateSpecification.update_forward_refs()
