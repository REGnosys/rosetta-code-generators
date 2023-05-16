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

__all__ = ['OptionFeature']


class OptionFeature(BaseDataClass):
  """
  Defines additional optional features that can be included in an option contract.
  """
  averagingFeature: Optional[AveragingCalculation] = Field(None, description="Defines an option feature in which an average market observation price is determined on valuation and compared to the strike to determine a settlement amount.")
  """
  Defines an option feature in which an average market observation price is determined on valuation and compared to the strike to determine a settlement amount.
  """
  barrier: Optional[Barrier] = Field(None, description="Specifies a barrier feature.")
  """
  Specifies a barrier feature.
  """
  fxFeature: List[FxFeature] = Field([], description="Describes a quanto or composite FX feature.")
  """
  Describes a quanto or composite FX feature.
  """
  knock: Optional[Knock] = Field(None, description="Specifies a knock in or knock out feature.")
  """
  Specifies a knock in or knock out feature.
  """
  passThrough: Optional[PassThrough] = Field(None, description="Specifies the rules for pass-through payments from the underlier, such as dividends.")
  """
  Specifies the rules for pass-through payments from the underlier, such as dividends.
  """
  strategyFeature: Optional[StrategyFeature] = Field(None, description="Defines a simple strategy feature.")
  """
  Defines a simple strategy feature.
  """

from cdm.product.template.AveragingCalculation import AveragingCalculation
from cdm.product.template.Barrier import Barrier
from cdm.product.template.FxFeature import FxFeature
from cdm.product.template.Knock import Knock
from cdm.product.template.PassThrough import PassThrough
from cdm.product.template.StrategyFeature import StrategyFeature

OptionFeature.update_forward_refs()
