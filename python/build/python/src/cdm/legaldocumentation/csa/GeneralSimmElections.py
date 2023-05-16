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

__all__ = ['GeneralSimmElections']


class GeneralSimmElections(BaseDataClass):
  """
  A class to specify the ISDA SIMM as the Method for all Covered Transactions with respect to all Regimes. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (ee).
  """
  simmCalculationCurrency: SimmCalculationCurrency = Field(..., description="The SIMM Calculation Currency, as specified for each of the parties to the CSA Initial Margin. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (ee)(3).")
  """
  The SIMM Calculation Currency, as specified for each of the parties to the CSA Initial Margin. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (ee)(3).
  """
  simmVersion: Optional[SimmVersion] = Field(None, description="The qualification of the ISDA SIMM version that is specified for all Covered Transactions as specified by ISDA 2018 CSA for Initial Margin, Paragraph 13, General Principles, (ee)(1).")
  """
  The qualification of the ISDA SIMM version that is specified for all Covered Transactions as specified by ISDA 2018 CSA for Initial Margin, Paragraph 13, General Principles, (ee)(1).
  """

from cdm.legaldocumentation.csa.SimmCalculationCurrency import SimmCalculationCurrency
from cdm.legaldocumentation.csa.SimmVersion import SimmVersion

GeneralSimmElections.update_forward_refs()
