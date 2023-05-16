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

__all__ = ['ForeignExchange']


class ForeignExchange(BaseDataClass):
  """
  From FpML: A type defining either a spot or forward FX transactions.
  """
  exchangeRate: Optional[ExchangeRate] = Field(None, description="The rate of exchange between the two currencies.")
  """
  The rate of exchange between the two currencies.
  """
  exchangedCurrency1: Cashflow = Field(..., description="This is the first of the two currency flows that define a single leg of a standard foreign exchange transaction.")
  """
  This is the first of the two currency flows that define a single leg of a standard foreign exchange transaction.
  """
  exchangedCurrency2: Cashflow = Field(..., description="This is the second of the two currency flows that define a single leg of a standard foreign exchange transaction.")
  """
  This is the second of the two currency flows that define a single leg of a standard foreign exchange transaction.
  """
  tenorPeriod: Optional[Period] = Field(None, description="A tenor expressed as a period type and multiplier (e.g. 1D, 1Y, etc.)")
  """
  A tenor expressed as a period type and multiplier (e.g. 1D, 1Y, etc.)
  """

from cdm.observable.asset.ExchangeRate import ExchangeRate
from cdm.product.common.settlement.Cashflow import Cashflow
from cdm.base.datetime.Period import Period

ForeignExchange.update_forward_refs()
