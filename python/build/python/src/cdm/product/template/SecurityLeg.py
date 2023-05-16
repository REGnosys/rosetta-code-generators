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

__all__ = ['SecurityLeg']


class SecurityLeg(BaseDataClass):
  """
   Terms defining a security leg in a securities financing transaction, which can either be the near leg or the far leg and is closely modelled onto the nearLeg and farLeg types in FpML
  """
  buyerSeller: BuyerSeller = Field(..., description="Whether the leg is a buyer or seller of security")
  """
  Whether the leg is a buyer or seller of security
  """
  deliveryDate: Optional[AdjustableOrRelativeDate] = Field(None, description="Delivery Date for the transaction. Delivery Date can be populated when it is not equal to the Settlement Date.")
  """
  Delivery Date for the transaction. Delivery Date can be populated when it is not equal to the Settlement Date.
  """
  deliveryMethod: DeliveryMethodEnum = Field(..., description="Specifies a delivery method for the security transaction.")
  """
  Specifies a delivery method for the security transaction.
  """
  fxRate: Optional[ExchangeRate] = Field(None, description="FX rate in case when cash settlement amount is in a different currency to the security.")
  """
  FX rate in case when cash settlement amount is in a different currency to the security.
  """
  settlementAmount: Optional[Money] = Field(None, description="Settlement amount for the security leg")
  """
  Settlement amount for the security leg
  """
  settlementCurrency: Optional[str] = Field(None, description="Settlement Currency for use where the Settlement Amount cannot be known in advance.")
  """
  Settlement Currency for use where the Settlement Amount cannot be known in advance.
  """
  settlementDate: AdjustableOrRelativeDate = Field(..., description="Settlement or Payment Date for the security leg")
  """
  Settlement or Payment Date for the security leg
  """
  
  @rosetta_condition
  def condition_0_SecurityLegChoice(self):
    return self.check_one_of_constraint('settlementAmount', 'settlementCurrency', necessity=True)

from cdm.base.staticdata.party.BuyerSeller import BuyerSeller
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.product.common.settlement.DeliveryMethodEnum import DeliveryMethodEnum
from cdm.observable.asset.ExchangeRate import ExchangeRate
from cdm.observable.asset.Money import Money

SecurityLeg.update_forward_refs()
