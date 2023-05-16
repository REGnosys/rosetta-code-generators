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

__all__ = ['DebtType']


class DebtType(BaseDataClass):
  """
  Specifies the type of debt instrument.
  """
  debtClass: Optional[DebtClassEnum] = Field(None, description="Specifies the characteristics of a debt instrument.")
  """
  Specifies the characteristics of a debt instrument.
  """
  debtEconomics: List[DebtEconomics] = Field([], description="Specifies selected financial terms of a debt instrument.")
  """
  Specifies selected financial terms of a debt instrument.
  """

from cdm.base.staticdata.asset.common.DebtClassEnum import DebtClassEnum
from cdm.base.staticdata.asset.common.DebtEconomics import DebtEconomics

DebtType.update_forward_refs()
