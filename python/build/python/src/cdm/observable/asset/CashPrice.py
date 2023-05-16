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

__all__ = ['CashPrice']


class CashPrice(BaseDataClass):
  """
  Specifies the nature of a cash price either as a fee type, cash price type, or premium expression.
  """
  cashPriceType: CashPriceTypeEnum = Field(..., description="Specifies the type of Cash Price.")
  """
  Specifies the type of Cash Price.
  """
  feeType: Optional[FeeTypeEnum] = Field(None, description="Specifies the event type associated with a fee.")
  """
  Specifies the event type associated with a fee.
  """
  premiumExpression: Optional[PremiumExpression] = Field(None, description="Specifies a premium when expressed in a way other than an amount, and any required forward starting price definition.")
  """
  Specifies a premium when expressed in a way other than an amount, and any required forward starting price definition.
  """
  
  @rosetta_condition
  def condition_0_PremiumType(self):
    """
    Premium type can only be specified when the cash price type is a premium.
    """
    def _then_fn0():
      return all_elements(self.cashPriceType, "=", CashPriceTypeEnum.PREMIUM)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.premiumExpression) is not None), _then_fn0, _else_fn0)

from cdm.observable.asset.CashPriceTypeEnum import CashPriceTypeEnum
from cdm.observable.asset.FeeTypeEnum import FeeTypeEnum
from cdm.observable.asset.PremiumExpression import PremiumExpression

CashPrice.update_forward_refs()
