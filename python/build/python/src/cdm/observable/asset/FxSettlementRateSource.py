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

__all__ = ['FxSettlementRateSource']


class FxSettlementRateSource(BaseDataClass):
  """
  The source of the Foreign Exchange settlement rate.
  """
  nonstandardSettlementRate: Optional[FxInformationSource] = Field(None, description="Indicates that a non-standard rate source will be used for the fixing.")
  """
  Indicates that a non-standard rate source will be used for the fixing.
  """
  settlementRateOption: Optional[AttributeWithMeta[str] | str] = Field(None, description="Indicates that an officially defined rate settlement rate option will be the used for the fixing.")
  """
  Indicates that an officially defined rate settlement rate option will be the used for the fixing.
  """
  
  @rosetta_condition
  def condition_0_FxSettlementRateSourceChoice(self):
    return self.check_one_of_constraint('settlementRateOption', 'nonstandardSettlementRate', necessity=True)

from cdm.observable.asset.FxInformationSource import FxInformationSource

FxSettlementRateSource.update_forward_refs()
