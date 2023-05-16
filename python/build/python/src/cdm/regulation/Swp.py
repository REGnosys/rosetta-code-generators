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

__all__ = ['Swp']


class Swp(BaseDataClass):
  swpIn: SwpIn = Field(..., description="")
  swpOut: SwpOut = Field(..., description="")

from cdm.regulation.SwpIn import SwpIn
from cdm.regulation.SwpOut import SwpOut

Swp.update_forward_refs()
