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

__all__ = ['MandatoryEarlyTermination']


class MandatoryEarlyTermination(BaseDataClass):
  """
  A data to:  define an early termination provision for which exercise is mandatory.
  """
  calculationAgent: CalculationAgent = Field(..., description="The ISDA Calculation Agent responsible for performing duties associated with an optional early termination.")
  """
  The ISDA Calculation Agent responsible for performing duties associated with an optional early termination.
  """
  cashSettlement: SettlementTerms = Field(..., description="If specified, this means that cash settlement is applicable to the transaction and defines the parameters associated with the cash settlement procedure. If not specified, then physical settlement is applicable.")
  """
  If specified, this means that cash settlement is applicable to the transaction and defines the parameters associated with the cash settlement procedure. If not specified, then physical settlement is applicable.
  """
  mandatoryEarlyTerminationAdjustedDates: Optional[MandatoryEarlyTerminationAdjustedDates] = Field(None, description="The adjusted dates associated with a mandatory early termination provision. These dates have been adjusted for any applicable business day convention.")
  """
  The adjusted dates associated with a mandatory early termination provision. These dates have been adjusted for any applicable business day convention.
  """
  mandatoryEarlyTerminationDate: AdjustableDate = Field(..., description="The early termination date associated with a mandatory early termination of a swap.")
  """
  The early termination date associated with a mandatory early termination of a swap.
  """
  
  @rosetta_condition
  def condition_0_MandatoryEarlyTerminationCalculationAgent(self):
    def _then_fn0():
      return all_elements(self.calculationAgent.calculationAgentParty, "=", AncillaryRoleEnum.CALCULATION_AGENT_MANDATORY_EARLY_TERMINATION)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.calculationAgent.calculationAgentParty) is not None), _then_fn0, _else_fn0)

from cdm.observable.asset.CalculationAgent import CalculationAgent
from cdm.product.common.settlement.SettlementTerms import SettlementTerms
from cdm.product.template.MandatoryEarlyTerminationAdjustedDates import MandatoryEarlyTerminationAdjustedDates
from cdm.base.datetime.AdjustableDate import AdjustableDate
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

MandatoryEarlyTermination.update_forward_refs()
