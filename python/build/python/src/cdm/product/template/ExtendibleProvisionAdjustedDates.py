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

__all__ = ['ExtendibleProvisionAdjustedDates']


class ExtendibleProvisionAdjustedDates(BaseDataClass):
  """
  A data defining:  the adjusted dates associated with a provision to extend a swap.
  """
  extensionEvent: List[ExtensionEvent] = Field([], description="The adjusted dates associated with a single extendible exercise date.")
  """
  The adjusted dates associated with a single extendible exercise date.
  """
  @rosetta_condition
  def cardinality_extensionEvent(self):
    return check_cardinality(self.extensionEvent, 1, None)
  

from cdm.product.template.ExtensionEvent import ExtensionEvent

ExtendibleProvisionAdjustedDates.update_forward_refs()
