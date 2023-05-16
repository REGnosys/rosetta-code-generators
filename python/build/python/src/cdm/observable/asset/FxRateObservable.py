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

__all__ = ['FxRateObservable']


class FxRateObservable(BaseDataClass):
  """
  Defines foreign exchange (FX) asset class specific parameters for market observations.
  """
  primaryFxSpotRateSource: InformationSource = Field(..., description="Specifies the primary source from which a rate should be observed.")
  """
  Specifies the primary source from which a rate should be observed.
  """
  quotedCurrencyPair: AttributeWithAddress[QuotedCurrencyPair] | QuotedCurrencyPair = Field(..., description="Describes the composition of a rate that has been quoted or is to be quoted.")
  """
  Describes the composition of a rate that has been quoted or is to be quoted.
  """
  secondaryFxSpotRateSource: Optional[InformationSource] = Field(None, description="Specifies an alternative, or secondary, source from which a rate should be observed.")
  """
  Specifies an alternative, or secondary, source from which a rate should be observed.
  """

from cdm.observable.asset.InformationSource import InformationSource
from cdm.observable.asset.QuotedCurrencyPair import QuotedCurrencyPair

FxRateObservable.update_forward_refs()
