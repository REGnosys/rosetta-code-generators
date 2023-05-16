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

__all__ = ['StrikeSpread']


class StrikeSpread(BaseDataClass):
  """
  A class for defining a strike spread feature.
  """
  upperStrike: OptionStrike = Field(..., description="Upper strike in a strike spread.")
  """
  Upper strike in a strike spread.
  """
  upperStrikeNumberOfOptions: Decimal = Field(..., description="Number of options at the upper strike price in a strike spread.")
  """
  Number of options at the upper strike price in a strike spread.
  """

from cdm.product.template.OptionStrike import OptionStrike

StrikeSpread.update_forward_refs()
