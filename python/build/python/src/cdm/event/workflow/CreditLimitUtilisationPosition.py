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

__all__ = ['CreditLimitUtilisationPosition']


class CreditLimitUtilisationPosition(BaseDataClass):
  _global: Optional[Decimal] = Field(None, description="Global credit limit utilisation amount, agnostic of long/short position direction.")
  """
  Global credit limit utilisation amount, agnostic of long/short position direction.
  """
  longPosition: Optional[Decimal] = Field(None, description="Credit limit utilisation attributable to long positions.")
  """
  Credit limit utilisation attributable to long positions.
  """
  shortPosition: Optional[Decimal] = Field(None, description="Credit limit utilisation attributable to short positions.")
  """
  Credit limit utilisation attributable to short positions.
  """


CreditLimitUtilisationPosition.update_forward_refs()
