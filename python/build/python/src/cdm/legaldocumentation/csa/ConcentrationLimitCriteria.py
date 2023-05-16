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

__all__ = ['ConcentrationLimitCriteria']

from cdm.legaldocumentation.csa.CollateralCriteriaBase import CollateralCriteriaBase

class ConcentrationLimitCriteria(CollateralCriteriaBase):
  """
  Respresents a class to describe a set of criteria to describe specific assets that the concentration limits apply to.
  """
  averageTradingVolume: Optional[AverageTradingVolume] = Field(None, description="Specifies an average trading volume on an exchange in relation to Equity products.")
  """
  Specifies an average trading volume on an exchange in relation to Equity products.
  """
  concentrationLimitType: Optional[ConcentrationLimitTypeEnum] = Field(None, description="Specifies the type of concentration limit to be applied.")
  """
  Specifies the type of concentration limit to be applied.
  """
  
  @rosetta_condition
  def condition_0_ConcentrationLimitTypeChoice(self):
    """
    Either a limit type or limit criteria must be specified.
    """
    return self.check_one_of_constraint('concentrationLimitType', 'issuer', 'asset', 'averageTradingVolume', necessity=True)

from cdm.legaldocumentation.csa.AverageTradingVolume import AverageTradingVolume
from cdm.legaldocumentation.csa.ConcentrationLimitTypeEnum import ConcentrationLimitTypeEnum

ConcentrationLimitCriteria.update_forward_refs()
