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

__all__ = ['PassThrough']


class PassThrough(BaseDataClass):
  """
  Type which contains pass through payments.
  """
  passThroughItem: List[PassThroughItem] = Field([], description="One to many pass through payment items.")
  """
  One to many pass through payment items.
  """
  @rosetta_condition
  def cardinality_passThroughItem(self):
    return check_cardinality(self.passThroughItem, 1, None)
  

from cdm.product.template.PassThroughItem import PassThroughItem

PassThrough.update_forward_refs()
