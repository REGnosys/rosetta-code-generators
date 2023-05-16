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

__all__ = ['SensitivityMethodologies']


class SensitivityMethodologies(BaseDataClass):
  """
  A class to specificy methodologies to compute sensitivities specific to the agreement.
  """
  sensitivityToCommodity: SensitivityMethodology = Field(..., description="The methodology to compute sensitivities to commodity indices for the purpose of Initial Margin agreements.")
  """
  The methodology to compute sensitivities to commodity indices for the purpose of Initial Margin agreements.
  """
  sensitivityToEquity: SensitivityMethodology = Field(..., description="The methodology to compute sensitivities to equity indices, funds and ETFs for the purpose of Initial Margin agreements.")
  """
  The methodology to compute sensitivities to equity indices, funds and ETFs for the purpose of Initial Margin agreements.
  """

from cdm.legaldocumentation.csa.SensitivityMethodology import SensitivityMethodology

SensitivityMethodologies.update_forward_refs()
