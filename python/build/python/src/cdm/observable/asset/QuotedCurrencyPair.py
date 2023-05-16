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

__all__ = ['QuotedCurrencyPair']


class QuotedCurrencyPair(BaseDataClass):
  """
  A class that describes the composition of a rate that has been quoted or is to be quoted. This includes the two currencies and the quotation relationship between the two currencies and is used as a building block throughout the FX specification.
  """
  currency1: AttributeWithMeta[str] | str = Field(..., description="The first currency specified when a pair of currencies is to be evaluated.")
  """
  The first currency specified when a pair of currencies is to be evaluated.
  """
  currency2: AttributeWithMeta[str] | str = Field(..., description="The second currency specified when a pair of currencies is to be evaluated.")
  """
  The second currency specified when a pair of currencies is to be evaluated.
  """
  quoteBasis: QuoteBasisEnum = Field(..., description="The method by which the exchange rate is quoted.")
  """
  The method by which the exchange rate is quoted.
  """

from cdm.observable.asset.QuoteBasisEnum import QuoteBasisEnum

QuotedCurrencyPair.update_forward_refs()
