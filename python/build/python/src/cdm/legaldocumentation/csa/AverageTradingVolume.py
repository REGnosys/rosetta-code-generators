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

__all__ = ['AverageTradingVolume']


class AverageTradingVolume(BaseDataClass):
  """
  Represents the average trading volume of an Equity product upon an exchange or set of exchanges.
  """
  methodology: AverageTradingVolumeMethodologyEnum = Field(..., description="Indicates the type of equity average trading volume being stated (single) the highest amount on one exchange, or (consolidated) volumes across multiple exchanges.")
  """
  Indicates the type of equity average trading volume being stated (single) the highest amount on one exchange, or (consolidated) volumes across multiple exchanges.
  """
  period: Period = Field(..., description="Represents the period of the equities average trading volume on the exchange/s.")
  """
  Represents the period of the equities average trading volume on the exchange/s.
  """

from cdm.legaldocumentation.csa.AverageTradingVolumeMethodologyEnum import AverageTradingVolumeMethodologyEnum
from cdm.base.datetime.Period import Period

AverageTradingVolume.update_forward_refs()
