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

__all__ = ['DiscountingMethod']


class DiscountingMethod(BaseDataClass):
  """
  A data defining:  discounting information. The 2000 ISDA definitions, section 8.4. discounting (related to the calculation of a discounted fixed amount or floating amount) apply. This type must only be included if discounting applies.
  """
  discountRate: Optional[Decimal] = Field(None, description="A discount rate, expressed as a decimal, to be used in the calculation of a discounted amount. A discount amount of 5% would be represented as 0.05.")
  """
  A discount rate, expressed as a decimal, to be used in the calculation of a discounted amount. A discount amount of 5% would be represented as 0.05.
  """
  discountRateDayCountFraction: Optional[AttributeWithMeta[DayCountFractionEnum] | DayCountFractionEnum] = Field(None, description="A discount day count fraction to be used in the calculation of a discounted amount.")
  """
  A discount day count fraction to be used in the calculation of a discounted amount.
  """
  discountingType: DiscountingTypeEnum = Field(..., description="The discounting method that is applicable.")
  """
  The discounting method that is applicable.
  """
  
  @rosetta_condition
  def condition_0_DiscountRate(self):
    """
    In FpML discountingRate and discountRateDayCountFraction are part of an optional node, with discountingRate as the required element as part of that node.
    """
    def _then_fn0():
      return ((self.discountRate) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.discountRateDayCountFraction) is not None), _then_fn0, _else_fn0)

from cdm.base.datetime.daycount.DayCountFractionEnum import DayCountFractionEnum
from cdm.product.asset.DiscountingTypeEnum import DiscountingTypeEnum

DiscountingMethod.update_forward_refs()
