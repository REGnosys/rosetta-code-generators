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

__all__ = ['RelativePrice']


class RelativePrice(BaseDataClass):
  """
   Bond price relative to a benchmark, as in a convertible bond.
  """
  bondEquityModel: List[BondEquityModel] = Field([], description="Bond equity model for convertible bonds.")
  """
  Bond equity model for convertible bonds.
  """
  @rosetta_condition
  def cardinality_bondEquityModel(self):
    return check_cardinality(self.bondEquityModel, 1, None)
  
  spread: Decimal = Field(..., description="The spread to a benchmark.")
  """
  The spread to a benchmark.
  """

from cdm.observable.asset.BondEquityModel import BondEquityModel

RelativePrice.update_forward_refs()
