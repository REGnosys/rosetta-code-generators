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

__all__ = ['CleanPrice']


class CleanPrice(BaseDataClass):
  """
   Class to specify the clean price of a bond in a bond valuation model, with accruals presented separately, and modelled onto the cleanPrice model in BonPriceAndYield.model in FpML.
  """
  accruals: Optional[Decimal] = Field(None, description="The accruals as a number.")
  """
  The accruals as a number.
  """
  cleanPrice: Decimal = Field(..., description="The clean price as a number.")
  """
  The clean price as a number.
  """
  dirtyPrice: Optional[str] = Field(None, description="Placeholder for a calculation of dirtyPrice based on cleanPrice and accruals.")
  """
  Placeholder for a calculation of dirtyPrice based on cleanPrice and accruals.
  """


CleanPrice.update_forward_refs()
