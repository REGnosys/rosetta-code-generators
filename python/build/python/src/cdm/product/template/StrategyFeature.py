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

__all__ = ['StrategyFeature']


class StrategyFeature(BaseDataClass):
  """
  A class for defining option strategy features.
  """
  calendarSpread: Optional[CalendarSpread] = Field(None, description="Definition of the later expiration date in a calendar spread.")
  """
  Definition of the later expiration date in a calendar spread.
  """
  strikeSpread: Optional[StrikeSpread] = Field(None, description="Definition of the upper strike in a strike spread.")
  """
  Definition of the upper strike in a strike spread.
  """

from cdm.product.template.CalendarSpread import CalendarSpread
from cdm.product.template.StrikeSpread import StrikeSpread

StrategyFeature.update_forward_refs()
