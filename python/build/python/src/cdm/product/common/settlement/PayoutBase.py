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

__all__ = ['PayoutBase']


class PayoutBase(BaseDataClass):
  """
   Base class that all payout types should extend. Use case is that some validation rules may need to apply across all payout types, for which the data rule can be written at the base class level
  """
  payerReceiver: PayerReceiver = Field(..., description="Canonical representation of the payer and receiver parties applicable to each payout leg.")
  """
  Canonical representation of the payer and receiver parties applicable to each payout leg.
  """
  priceQuantity: Optional[ResolvablePriceQuantity] = Field(None, description="Each payout leg must implement the quantity concept as a 'resolvable' type, which allows for different payout legs to be linked to each other (e.g. in the case of cross-curreny products).")
  """
  Each payout leg must implement the quantity concept as a 'resolvable' type, which allows for different payout legs to be linked to each other (e.g. in the case of cross-curreny products).
  """
  principalPayment: Optional[PrincipalPayments] = Field(None, description="The specification of the principal exchange. Optional as only applicable in the case of cross-currency or zero-coupon swaps with a final payment.")
  """
  The specification of the principal exchange. Optional as only applicable in the case of cross-currency or zero-coupon swaps with a final payment.
  """
  settlementTerms: Optional[SettlementTerms] = Field(None, description="Each payout leg must specifies its settlement terms, including the delivery type (i.e. cash vs physical, and their respective terms), the transfer type (DvP etc.) and settlement date, if any.")
  """
  Each payout leg must specifies its settlement terms, including the delivery type (i.e. cash vs physical, and their respective terms), the transfer type (DvP etc.) and settlement date, if any.
  """

from cdm.base.staticdata.party.PayerReceiver import PayerReceiver
from cdm.product.common.settlement.ResolvablePriceQuantity import ResolvablePriceQuantity
from cdm.product.common.settlement.PrincipalPayments import PrincipalPayments
from cdm.product.common.settlement.SettlementTerms import SettlementTerms

PayoutBase.update_forward_refs()
