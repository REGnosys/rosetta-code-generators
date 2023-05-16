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

__all__ = ['DividendPaymentDate']


class DividendPaymentDate(BaseDataClass):
  """
  A class describing the date on which the dividend will be paid/received. This class is also used to specify the date on which the FX rate will be determined, when applicable.
  """
  dividendDate: Optional[AttributeWithReference | AdjustableOrRelativeDate] = Field(None, description="")
  dividendDateReference: Optional[DividendDateReference] = Field(None, description="")
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('dividendDateReference', 'dividendDate', necessity=True)

from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.product.asset.DividendDateReference import DividendDateReference

DividendPaymentDate.update_forward_refs()
