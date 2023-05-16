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

__all__ = ['PercentageRule']


class PercentageRule(BaseDataClass):
  """
  A class defining a content model for a calculation rule defined as percentage of the notional amount.
  """
  notionalAmountReference: AttributeWithReference | Money = Field(..., description="A reference to the notional amount.")
  """
  A reference to the notional amount.
  """
  paymentPercent: Decimal = Field(..., description="A percentage of the notional amount.")
  """
  A percentage of the notional amount.
  """

from cdm.observable.asset.Money import Money

PercentageRule.update_forward_refs()
