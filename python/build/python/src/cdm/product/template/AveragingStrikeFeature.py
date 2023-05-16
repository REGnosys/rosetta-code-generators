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

__all__ = ['AveragingStrikeFeature']


class AveragingStrikeFeature(BaseDataClass):
  """
  Defines the terms required to calculate the average observations associated with an averaging strike.
  """
  averagingCalculation: AveragingCalculation = Field(..., description="Defines parameters for use in cases when a valuation or other term is based on an average of market observations.")
  """
  Defines parameters for use in cases when a valuation or other term is based on an average of market observations.
  """
  observationTerms: ObservationTerms = Field(..., description="Class containing terms that are associated with observing a price/benchmark/index across either single or multple observations. ")
  """
  Class containing terms that are associated with observing a price/benchmark/index across either single or multple observations. 
  """

from cdm.product.template.AveragingCalculation import AveragingCalculation
from cdm.product.common.schedule.ObservationTerms import ObservationTerms

AveragingStrikeFeature.update_forward_refs()
