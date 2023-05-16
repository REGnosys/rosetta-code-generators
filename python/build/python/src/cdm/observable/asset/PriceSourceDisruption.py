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

__all__ = ['PriceSourceDisruption']


class PriceSourceDisruption(BaseDataClass):
  """
  A data defining:  the parameters used to get a price quote to replace the settlement rate option that is disrupted.
  """
  fallbackReferencePrice: FallbackReferencePrice = Field(..., description="The method, prioritised by the order it is listed in this element, to get a replacement rate for the disrupted settlement rate option.")
  """
  The method, prioritised by the order it is listed in this element, to get a replacement rate for the disrupted settlement rate option.
  """

from cdm.observable.asset.FallbackReferencePrice import FallbackReferencePrice

PriceSourceDisruption.update_forward_refs()
