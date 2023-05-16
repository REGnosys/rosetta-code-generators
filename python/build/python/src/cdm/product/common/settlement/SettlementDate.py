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

__all__ = ['SettlementDate']


class SettlementDate(BaseDataClass):
  """
  A data defining the settlement date(s) for cash or physical settlement as either a set of explicit dates, together with applicable adjustments, or as a date relative to some other (anchor) date, or as any date in a range of contiguous business days. This data type provides a level of abstraction on top of the different legacy methods used to specify a settlement / payment date, which vary across product types, asset classes and delivery types.
  """
  adjustableDates: Optional[AdjustableDates] = Field(None, description="A series of dates that shall be subject to adjustment if they would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date. This attributes was formerly part of 'CashSettlementPaymentDate' as included into 'OptionCashSettlement' (which is now merged into a unique 'CashSettlementTerms' data type.")
  """
  A series of dates that shall be subject to adjustment if they would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date. This attributes was formerly part of 'CashSettlementPaymentDate' as included into 'OptionCashSettlement' (which is now merged into a unique 'CashSettlementTerms' data type.
  """
  adjustableOrRelativeDate: Optional[AdjustableOrAdjustedOrRelativeDate] = Field(None, description="A single settlement date subject to adjustment or specified as relative to another date (e.g. the trade date). This attribute was formerly part of 'SettlementTerms', which is now being harmonised to include a common 'SettlementDate', as inherited from 'SettlementBase'.")
  """
  A single settlement date subject to adjustment or specified as relative to another date (e.g. the trade date). This attribute was formerly part of 'SettlementTerms', which is now being harmonised to include a common 'SettlementDate', as inherited from 'SettlementBase'.
  """
  businessDateRange: Optional[BusinessDateRange] = Field(None, description="A range of contiguous business days. This attribute is meant to be merged with the 'settlementDate' at some future point once we refactor 'Date' to use a single complex type across the model. This attributes was formerly part of 'CashSettlementPaymentDate', as included into 'OptionCashSettlement' (which is now merged into a unique 'CashSettlementTerms' data type.")
  """
  A range of contiguous business days. This attribute is meant to be merged with the 'settlementDate' at some future point once we refactor 'Date' to use a single complex type across the model. This attributes was formerly part of 'CashSettlementPaymentDate', as included into 'OptionCashSettlement' (which is now merged into a unique 'CashSettlementTerms' data type.
  """
  cashSettlementBusinessDays: Optional[int] = Field(None, description="The number of business days used in the determination of the cash settlement payment date. If a cash settlement amount is specified, the cash settlement payment date will be this number of business days following the calculation of the final price. If a cash settlement amount is not specified, the cash settlement payment date will be this number of business days after all conditions to settlement are satisfied. ISDA 2003 Term: Cash Settlement Date. This attribute was formerly part of 'CashSettlementTerms' as used for credit event settlement, which now includes a common 'SettlementDate' attribute.")
  """
  The number of business days used in the determination of the cash settlement payment date. If a cash settlement amount is specified, the cash settlement payment date will be this number of business days following the calculation of the final price. If a cash settlement amount is not specified, the cash settlement payment date will be this number of business days after all conditions to settlement are satisfied. ISDA 2003 Term: Cash Settlement Date. This attribute was formerly part of 'CashSettlementTerms' as used for credit event settlement, which now includes a common 'SettlementDate' attribute.
  """
  paymentDelay: Optional[bool] = Field(None, description="Applicable to CDS on MBS to specify whether payment delays are applicable to the fixed Amount. RMBS typically have a payment delay of 5 days between the coupon date of the reference obligation and the payment date of the synthetic swap. CMBS do not, on the other hand, with both payment dates being on the 25th of each month.")
  """
  Applicable to CDS on MBS to specify whether payment delays are applicable to the fixed Amount. RMBS typically have a payment delay of 5 days between the coupon date of the reference obligation and the payment date of the synthetic swap. CMBS do not, on the other hand, with both payment dates being on the 25th of each month.
  """
  valueDate: Optional[date] = Field(None, description="The settlement date for a forward settling product. For Foreign Exchange contracts, this represents a common settlement date between both currency legs. To specify different settlement dates for each currency leg, see the ForeignExchange class. This attribute was formerly part of 'SettlementTerms', which is now being harmonised to include a common 'SettlementDate', as inherited from 'SettlementBase'.")
  """
  The settlement date for a forward settling product. For Foreign Exchange contracts, this represents a common settlement date between both currency legs. To specify different settlement dates for each currency leg, see the ForeignExchange class. This attribute was formerly part of 'SettlementTerms', which is now being harmonised to include a common 'SettlementDate', as inherited from 'SettlementBase'.
  """
  
  @rosetta_condition
  def condition_0_BusinessDays(self):
    """
    FpML specifies cashSettlementBusinessDays as a nonNegativeInteger. If cashSettlementBusinessDays is not specified, then another settlement date method must be specified.
    """
    def _then_fn0():
      return all_elements(self.cashSettlementBusinessDays, ">=", 0)
    
    def _else_fn0():
      return (((((self.adjustableOrRelativeDate) is not None) or ((self.valueDate) is not None)) or ((self.adjustableDates) is not None)) or ((self.businessDateRange) is not None))
    
    return if_cond_fn(((self.cashSettlementBusinessDays) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_DateChoice(self):
    """
    Settlement date must be specified either throught the 'settlementDate' or 'valueDate' attribute. This is a temporary work-around until such time when we can retire the 'valueDate' attribute.
    """
    return self.check_one_of_constraint('adjustableOrRelativeDate', 'valueDate', 'adjustableDates', 'businessDateRange', necessity=False)

from cdm.base.datetime.AdjustableDates import AdjustableDates
from cdm.base.datetime.AdjustableOrAdjustedOrRelativeDate import AdjustableOrAdjustedOrRelativeDate
from cdm.base.datetime.BusinessDateRange import BusinessDateRange

SettlementDate.update_forward_refs()
