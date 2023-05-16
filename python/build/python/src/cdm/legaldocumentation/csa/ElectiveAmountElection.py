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

__all__ = ['ElectiveAmountElection']


class ElectiveAmountElection(BaseDataClass):
  """
  A class to specify the party elective amounts which can be used for the purpose of specifying elections such as the ISDA CSA Threshold and Minimum Transfer Amount.
  """
  amount: Optional[Money] = Field(None, description="The elective amount when expressed as a currency amount. The associated PartyElectiveAmount_amount data rule enforces that the currency amount is actually greater than 0.")
  """
  The elective amount when expressed as a currency amount. The associated PartyElectiveAmount_amount data rule enforces that the currency amount is actually greater than 0.
  """
  customElection: Optional[str] = Field(None, description="The elective amount when expressed as a custom election by the party.")
  """
  The elective amount when expressed as a custom election by the party.
  """
  electiveAmount: Optional[ElectiveAmountEnum] = Field(None, description="Specifies an enumerated election to express the elective amount.")
  """
  Specifies an enumerated election to express the elective amount.
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  
  @rosetta_condition
  def condition_0_NonZeroAmount(self):
    """
    When the elective amount is not zero either a currency amount or a custom election must exist.
    """
    def _then_fn0():
      return (((self.amount) is not None) or ((self.customElection) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.electiveAmount) is None), _then_fn0, _else_fn0)

from cdm.observable.asset.Money import Money
from cdm.legaldocumentation.csa.ElectiveAmountEnum import ElectiveAmountEnum
from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

ElectiveAmountElection.update_forward_refs()
