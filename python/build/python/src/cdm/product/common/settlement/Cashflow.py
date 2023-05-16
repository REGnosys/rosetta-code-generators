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

__all__ = ['Cashflow']

from cdm.product.common.settlement.PayoutBase import PayoutBase

class Cashflow(PayoutBase):
  """
  Class to specify a cashflow, i.e. the outcome of either of computation (e.g. interest accrual) or an assessment of some sort (e.g. a fee). The cashflow can then be turned into a cash transfer, artefact to be used as the input to a payment system or the outcome of it. The associated globalKey denotes the ability to associate a hash value to the Cashflow instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.
  """
  cashflowType: CashflowType = Field(..., description="The qualification of the type of cashflow, e.g. brokerage fee, premium, upfront fee etc. Particularly relevant when it cannot be inferred directly through lineage.")
  """
  The qualification of the type of cashflow, e.g. brokerage fee, premium, upfront fee etc. Particularly relevant when it cannot be inferred directly through lineage.
  """
  paymentDiscounting: Optional[PaymentDiscounting] = Field(None, description="FpML specifies the FpML PaymentDiscounting.model group for representing the discounting elements that can be associated with a payment.")
  """
  FpML specifies the FpML PaymentDiscounting.model group for representing the discounting elements that can be associated with a payment.
  """
  
  @rosetta_condition
  def condition_0_CashflowAmount(self):
    """
    The cashflow amount should be a positive number, as the cashflow direction is indeed implied by the payer/receiver attribute.
    """
    def _then_fn0():
      return all_elements(self.priceQuantity.quantitySchedule.value, ">=", 0.0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.priceQuantity) is not None), _then_fn0, _else_fn0)

from cdm.product.common.settlement.CashflowType import CashflowType
from cdm.product.common.settlement.PaymentDiscounting import PaymentDiscounting

Cashflow.update_forward_refs()
