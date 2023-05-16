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

__all__ = ['Restructuring']


class Restructuring(BaseDataClass):
  applicable: bool = Field(..., description="Indicates whether the restructuring provision is applicable.")
  """
  Indicates whether the restructuring provision is applicable.
  """
  multipleCreditEventNotices: Optional[bool] = Field(None, description="Presence of this element and value set to 'true' indicates that Section 3.9 of the 2003 Credit Derivatives Definitions shall apply. Absence of this element indicates that Section 3.9 shall not apply. NOTE: Not allowed under ISDA Credit 1999.")
  """
  Presence of this element and value set to 'true' indicates that Section 3.9 of the 2003 Credit Derivatives Definitions shall apply. Absence of this element indicates that Section 3.9 shall not apply. NOTE: Not allowed under ISDA Credit 1999.
  """
  multipleHolderObligation: Optional[bool] = Field(None, description="In relation to a restructuring credit event, unless multiple holder obligation is not specified restructurings are limited to multiple holder obligations. A multiple holder obligation means an obligation that is held by more than three holders that are not affiliates of each other and where at least two thirds of the holders must agree to the event that constitutes the restructuring credit event. ISDA 2003 Term: Multiple Holder Obligation.")
  """
  In relation to a restructuring credit event, unless multiple holder obligation is not specified restructurings are limited to multiple holder obligations. A multiple holder obligation means an obligation that is held by more than three holders that are not affiliates of each other and where at least two thirds of the holders must agree to the event that constitutes the restructuring credit event. ISDA 2003 Term: Multiple Holder Obligation.
  """
  restructuringType: Optional[AttributeWithMeta[RestructuringEnum] | RestructuringEnum] = Field(None, description="Specifies the type of restructuring that is applicable.")
  """
  Specifies the type of restructuring that is applicable.
  """

from cdm.observable.event.RestructuringEnum import RestructuringEnum

Restructuring.update_forward_refs()
