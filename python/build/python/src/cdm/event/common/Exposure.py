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

__all__ = ['Exposure']


class Exposure(BaseDataClass):
  """
  Represents the current mark to market value or IM calculation value of the trade portfolio as recorded by the principle (in base currency).
  """
  aggregateValue: Money = Field(..., description="Represents the aggregate value of the portfolio in base currency.")
  """
  Represents the aggregate value of the portfolio in base currency.
  """
  calculationDateTime: Optional[datetime] = Field(None, description="Indicates the date when the exposure is calculated if different from valuation date.")
  """
  Indicates the date when the exposure is calculated if different from valuation date.
  """
  tradePortfolio: AttributeWithReference | PortfolioState = Field(..., description="Represents a Portfolio that describes all the positions held at a given time, in various states which can be either traded, settled, etc., with lineage information to the previous state.")
  """
  Represents a Portfolio that describes all the positions held at a given time, in various states which can be either traded, settled, etc., with lineage information to the previous state.
  """
  valuationDateTime: datetime = Field(..., description="Indicates the valuation date of the exposure underlying the calculation.")
  """
  Indicates the valuation date of the exposure underlying the calculation.
  """

from cdm.observable.asset.Money import Money
from cdm.event.position.PortfolioState import PortfolioState

Exposure.update_forward_refs()
