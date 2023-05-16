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

__all__ = ['CustomisableOffset']


class CustomisableOffset(BaseDataClass):
  """
  A class to specify an offset either as a normalized [multiplier, period, dayType] or as a custom provision of type string.
  """
  customProvision: Optional[str] = Field(None, description="")
  offset: Optional[Offset] = Field(None, description="")

from cdm.base.datetime.Offset import Offset

CustomisableOffset.update_forward_refs()
