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

__all__ = ['FloatingRateIndexExternalMap']


class FloatingRateIndexExternalMap(BaseDataClass):
  """
  A map for a single FRO to or from an equivalent or similar codes in a different standard such as ISO.
  """
  externalId: str = Field(..., description=" The FRO name that is being mapped to/from.")
  """
   The FRO name that is being mapped to/from.
  """
  externalStandard: Optional[str] = Field(None, description="The standard/version to which the map applies.")
  """
  The standard/version to which the map applies.
  """


FloatingRateIndexExternalMap.update_forward_refs()
