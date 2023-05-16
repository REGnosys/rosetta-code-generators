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

__all__ = ['CorporateAction']


class CorporateAction(BaseDataClass):
  """
  Specifies the relevant data regarding a corporate action
  """
  corporateActionType: CorporateActionTypeEnum = Field(..., description="The type of corporate action taking place.")
  """
  The type of corporate action taking place.
  """
  exDate: date = Field(..., description="The date on which the corporate action is known to have taken place.")
  """
  The date on which the corporate action is known to have taken place.
  """
  payDate: date = Field(..., description="The date on which resulting from the corporate action are delivered.")
  """
  The date on which resulting from the corporate action are delivered.
  """
  underlier: Product = Field(..., description="The entity impacted by the corporate action.")
  """
  The entity impacted by the corporate action.
  """

from cdm.event.common.CorporateActionTypeEnum import CorporateActionTypeEnum
from cdm.product.template.Product import Product

CorporateAction.update_forward_refs()
