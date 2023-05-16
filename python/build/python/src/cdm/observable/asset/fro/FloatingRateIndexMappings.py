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

__all__ = ['FloatingRateIndexMappings']


class FloatingRateIndexMappings(BaseDataClass):
  """
  This type defines mappings between FROs in different definitional versions.
  """
  mapsFrom: List[FloatingRateIndexMap] = Field([], description="The predecessor FRO(s) that this index maps to.")
  """
  The predecessor FRO(s) that this index maps to.
  """
  mapsTo: Optional[FloatingRateIndexMap] = Field(None, description="The successor FRO that this index maps to.")
  """
  The successor FRO that this index maps to.
  """

from cdm.observable.asset.fro.FloatingRateIndexMap import FloatingRateIndexMap

FloatingRateIndexMappings.update_forward_refs()
