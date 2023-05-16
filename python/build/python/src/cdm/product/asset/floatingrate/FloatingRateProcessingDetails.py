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

__all__ = ['FloatingRateProcessingDetails']


class FloatingRateProcessingDetails(BaseDataClass):
  """
  Type for reporting the details of the rate treatment.  This could potentially be replaced by the existing FloatingRateDefinition type , but this is slightly more detailed.
  """
  processedRate: Decimal = Field(..., description="The value of the rate after processing.")
  """
  The value of the rate after processing.
  """
  processingParameters: Optional[FloatingRateProcessingParameters] = Field(None, description="")
  rawRate: Decimal = Field(..., description="The raw or untreated rate, prior to any of the rate treatments.")
  """
  The raw or untreated rate, prior to any of the rate treatments.
  """
  spreadExclusiveRate: Decimal = Field(..., description="The value of the processed rate without the spread applied, for subsequent compounding, etc.")
  """
  The value of the processed rate without the spread applied, for subsequent compounding, etc.
  """

from cdm.product.asset.floatingrate.FloatingRateProcessingParameters import FloatingRateProcessingParameters

FloatingRateProcessingDetails.update_forward_refs()
