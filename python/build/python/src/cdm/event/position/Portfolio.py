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

__all__ = ['Portfolio']


class Portfolio(BaseDataClass):
  """
   A Portfolio represents an aggregation of multiple Positions, by describing the parameters that this Portfolio should be aggregated based on. The resulting PortfolioState is calculated using these aggregation parameters as inputs, by aggregating all the Events that are relevant to this Portfolio. The concept of Portfolio works at all levels in the model: from the highest for a given LegalEntity for instance, to the lowest to account for security substitutions in a secutity financing transaction. As such, Portfolio can be used either above or below the Contract level.
  """
  aggregationParameters: AggregationParameters = Field(..., description="Describes the portfolio by describing how to aggregate all its relevant Events.")
  """
  Describes the portfolio by describing how to aggregate all its relevant Events.
  """
  portfolioState: PortfolioState = Field(..., description="Describes the state of the Portfolio as a list of Positions resulting from the aggregation.")
  """
  Describes the state of the Portfolio as a list of Positions resulting from the aggregation.
  """

from cdm.event.position.AggregationParameters import AggregationParameters
from cdm.event.position.PortfolioState import PortfolioState

Portfolio.update_forward_refs()
