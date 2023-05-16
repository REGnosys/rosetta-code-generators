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

__all__ = ['FxSpotRateSource']


class FxSpotRateSource(BaseDataClass):
  """
  A class defining the rate source and fixing time for an FX rate.
  """
  primarySource: InformationSource = Field(..., description="The primary source for where the rate observation will occur. Will typically be either a page or a reference bank published rate.")
  """
  The primary source for where the rate observation will occur. Will typically be either a page or a reference bank published rate.
  """
  secondarySource: Optional[InformationSource] = Field(None, description="An alternative, or secondary, source for where the rate observation will occur. Will typically be either a page or a reference bank published rate.")
  """
  An alternative, or secondary, source for where the rate observation will occur. Will typically be either a page or a reference bank published rate.
  """

from cdm.observable.asset.InformationSource import InformationSource

FxSpotRateSource.update_forward_refs()
