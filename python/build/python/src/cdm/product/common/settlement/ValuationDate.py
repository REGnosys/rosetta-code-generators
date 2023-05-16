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

__all__ = ['ValuationDate']


class ValuationDate(BaseDataClass):
  """
  A single object that represents the different methods to specify a valuation date, as used for cash settlement. The Single / Multiple ValuationDate is used for the determination of recovery in a credit event, the RelativeDateOffset is used for cash-settled option, and FxFixingDate is used for cross-currency settlement.
  """
  fxFixingDate: Optional[FxFixingDate] = Field(None, description="The date on which the currency rate will be determined for the purpose of specifying the amount in deliverable currency. This attribute was formerly part of 'NonDeliverableSettlement', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.")
  """
  The date on which the currency rate will be determined for the purpose of specifying the amount in deliverable currency. This attribute was formerly part of 'NonDeliverableSettlement', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.
  """
  fxFixingSchedule: Optional[AdjustableDates] = Field(None, description="The date, when expressed as a schedule of date(s), on which the currency rate will be determined for the purpose of specifying the amount in deliverable currency. This attribute was formerly part of 'NonDeliverableSettlement', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.")
  """
  The date, when expressed as a schedule of date(s), on which the currency rate will be determined for the purpose of specifying the amount in deliverable currency. This attribute was formerly part of 'NonDeliverableSettlement', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.
  """
  multipleValuationDates: Optional[MultipleValuationDates] = Field(None, description="Where multiple valuation dates are specified as being applicable for cash settlement, this element specifies (a) the number of applicable valuation dates, and (b) the number of business days after satisfaction of all conditions to settlement when the first such valuation date occurs, and (c) the number of business days thereafter of each successive valuation date. ISDA 2003 Term: Multiple Valuation Dates.")
  """
  Where multiple valuation dates are specified as being applicable for cash settlement, this element specifies (a) the number of applicable valuation dates, and (b) the number of business days after satisfaction of all conditions to settlement when the first such valuation date occurs, and (c) the number of business days thereafter of each successive valuation date. ISDA 2003 Term: Multiple Valuation Dates.
  """
  singleValuationDate: Optional[SingleValuationDate] = Field(None, description="Where single valuation date is specified as being applicable for cash settlement, this element specifies the number of business days after satisfaction of all conditions to settlement when such valuation date occurs. ISDA 2003 Term: Single Valuation Date.")
  """
  Where single valuation date is specified as being applicable for cash settlement, this element specifies the number of business days after satisfaction of all conditions to settlement when such valuation date occurs. ISDA 2003 Term: Single Valuation Date.
  """
  valuationDate: Optional[RelativeDateOffset] = Field(None, description="The date on which the cash settlement amount will be determined according to the cash settlement method if the parties have not otherwise been able to agree the cash settlement amount. This attribute was formerly part of 'OptionCashSettlement', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.")
  """
  The date on which the cash settlement amount will be determined according to the cash settlement method if the parties have not otherwise been able to agree the cash settlement amount. This attribute was formerly part of 'OptionCashSettlement', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('singleValuationDate', 'multipleValuationDates', 'valuationDate', 'fxFixingDate', 'fxFixingSchedule', necessity=True)

from cdm.product.common.settlement.FxFixingDate import FxFixingDate
from cdm.base.datetime.AdjustableDates import AdjustableDates
from cdm.observable.asset.MultipleValuationDates import MultipleValuationDates
from cdm.observable.asset.SingleValuationDate import SingleValuationDate
from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset

ValuationDate.update_forward_refs()
