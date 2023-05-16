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

__all__ = ['MoneyBound']


class MoneyBound(BaseDataClass):
  """
  The money bound is defined as a money amount and whether the bound is inclusive.
  """
  inclusive: bool = Field(..., description="Whether the money amount bound is inclusive, e.g. for a lower bound, false would indicate greater than, whereas true would indicate greater than or equal to.")
  """
  Whether the money amount bound is inclusive, e.g. for a lower bound, false would indicate greater than, whereas true would indicate greater than or equal to.
  """
  money: Money = Field(..., description="The money amount to be used as the bound, e.g. 1,000 USD.")
  """
  The money amount to be used as the bound, e.g. 1,000 USD.
  """

from cdm.observable.asset.Money import Money

MoneyBound.update_forward_refs()
