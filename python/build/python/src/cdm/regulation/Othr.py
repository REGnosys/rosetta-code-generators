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

__all__ = ['Othr']


class Othr(BaseDataClass):
  derivInstrmAttrbts: DerivInstrmAttrbts = Field(..., description="")
  finInstrmGnlAttrbts: FinInstrmGnlAttrbts = Field(..., description="")
  id: str = Field(..., description="")
  schmeNm: SchmeNm = Field(..., description="")

from cdm.regulation.DerivInstrmAttrbts import DerivInstrmAttrbts
from cdm.regulation.FinInstrmGnlAttrbts import FinInstrmGnlAttrbts
from cdm.regulation.SchmeNm import SchmeNm

Othr.update_forward_refs()
