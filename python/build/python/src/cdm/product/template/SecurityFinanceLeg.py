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

__all__ = ['SecurityFinanceLeg']


class SecurityFinanceLeg(BaseDataClass):
  """
  Defines each security movement of a security financing transaction.
  """
  deliveryMethod: DeliveryMethodEnum = Field(..., description="Specifies a delivery method for the security movement.")
  """
  Specifies a delivery method for the security movement.
  """
  settlementDate: AdjustableOrRelativeDate = Field(..., description="Settlement date of the security movement.")
  """
  Settlement date of the security movement.
  """

from cdm.product.common.settlement.DeliveryMethodEnum import DeliveryMethodEnum
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate

SecurityFinanceLeg.update_forward_refs()
