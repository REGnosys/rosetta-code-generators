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

__all__ = ['ExchangeRate']


class ExchangeRate(BaseDataClass):
  """
  A class that is used for describing the exchange rate for a particular transaction.
  """
  crossRate: List[CrossRate] = Field([], description="An optional element that allow for definition of the currency exchange rates used to cross between the traded currencies for non-base currency FX contracts.")
  """
  An optional element that allow for definition of the currency exchange rates used to cross between the traded currencies for non-base currency FX contracts.
  """

from cdm.observable.asset.CrossRate import CrossRate

ExchangeRate.update_forward_refs()
