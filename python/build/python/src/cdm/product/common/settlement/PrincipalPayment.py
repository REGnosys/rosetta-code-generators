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

__all__ = ['PrincipalPayment']


class PrincipalPayment(BaseDataClass):
  """
  Any kind of principal payments when the amount is known and thus fixed.
  """
  discountFactor: Optional[Decimal] = Field(None, description="The value representing the discount factor used to calculate the present value of the principal payment amount.")
  """
  The value representing the discount factor used to calculate the present value of the principal payment amount.
  """
  payerReceiver: Optional[PayerReceiver] = Field(None, description="Specifies the parties responsible for making and receiving payments defined by this structure.")
  """
  Specifies the parties responsible for making and receiving payments defined by this structure.
  """
  presentValuePrincipalAmount: Optional[Money] = Field(None, description="The amount representing the present value of the principal payment.")
  """
  The amount representing the present value of the principal payment.
  """
  principalAmount: Optional[Money] = Field(None, description="When known at the time the transaction is made, the cash amount to be paid.")
  """
  When known at the time the transaction is made, the cash amount to be paid.
  """
  principalPaymentDate: Optional[AdjustableDate] = Field(None, description="The date where the PrincipalPayment shall be settled.")
  """
  The date where the PrincipalPayment shall be settled.
  """
  
  @rosetta_condition
  def condition_0_PrincipalAmount(self):
    return self.check_one_of_constraint('principalAmount', 'presentValuePrincipalAmount', necessity=True)
  
  @rosetta_condition
  def condition_1_DiscountFactor(self):
    def _then_fn0():
      return ((self.discountFactor) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.presentValuePrincipalAmount) is not None), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.PayerReceiver import PayerReceiver
from cdm.observable.asset.Money import Money
from cdm.base.datetime.AdjustableDate import AdjustableDate

PrincipalPayment.update_forward_refs()
