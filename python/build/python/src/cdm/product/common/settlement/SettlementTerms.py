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

__all__ = ['SettlementTerms']

from cdm.product.common.settlement.SettlementBase import SettlementBase

class SettlementTerms(SettlementBase):
  """
  Specifies the settlement terms, which can either be cash, physical, or fx-based cash-settlement. This class can be used for the settlement of options and forwards, cash transactions (e.g. securities or foreign exchange), or in case of credit event.
  """
  cashSettlementTerms: List[CashSettlementTerms] = Field([], description="Specifies the parameters associated with the cash settlement procedure.")
  """
  Specifies the parameters associated with the cash settlement procedure.
  """
  physicalSettlementTerms: Optional[PhysicalSettlementTerms] = Field(None, description="Specifies the physical settlement terms which apply to the transaction.")
  """
  Specifies the physical settlement terms which apply to the transaction.
  """
  
  @rosetta_condition
  def condition_0_OptionSettlementChoice(self):
    """
    The option settlement cannot combine both physical and cash terms specification.
    """
    return self.check_one_of_constraint('cashSettlementTerms', 'physicalSettlementTerms', necessity=False)
  
  @rosetta_condition
  def condition_1_CashSettlementTerms(self):
    """
    If the cash settlement terms are specified, then the settlementType can either be Cash, Election or CashOrPhysical
    """
    def _then_fn0():
      return any_elements(self.settlementType, "<>", SettlementTypeEnum.PHYSICAL)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.cashSettlementTerms) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_PhysicalSettlementTerms(self):
    """
    If the physical settlement terms are specified, then the settlementType can either be Physical, Election or CashOrPhysical
    """
    def _then_fn0():
      return any_elements(self.settlementType, "<>", SettlementTypeEnum.CASH)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.physicalSettlementTerms) is not None), _then_fn0, _else_fn0)

from cdm.product.common.settlement.CashSettlementTerms import CashSettlementTerms
from cdm.product.common.settlement.PhysicalSettlementTerms import PhysicalSettlementTerms
from cdm.product.common.settlement.SettlementTypeEnum import SettlementTypeEnum

SettlementTerms.update_forward_refs()
