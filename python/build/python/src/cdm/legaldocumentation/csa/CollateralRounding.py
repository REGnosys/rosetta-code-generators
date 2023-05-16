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

__all__ = ['CollateralRounding']


class CollateralRounding(BaseDataClass):
  """
  A class to specify the rounding methodology applicable to the Delivery Amount and the Return Amount in terms of nearest integral multiple of Base Currency units. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (c)(vi)(C): Rounding. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(vi)(C): Rounding. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (c)(vi)(C): Rounding.
  """
  deliveryAmount: Decimal = Field(..., description="The rounding methodology applicable to the Delivery Amount in terms of nearest integral multiple of Base Currency units.")
  """
  The rounding methodology applicable to the Delivery Amount in terms of nearest integral multiple of Base Currency units.
  """
  returnAmount: Decimal = Field(..., description="The rounding methodology applicable to the Return Amount in terms of nearest integral multiple of Base Currency units.")
  """
  The rounding methodology applicable to the Return Amount in terms of nearest integral multiple of Base Currency units.
  """


CollateralRounding.update_forward_refs()
