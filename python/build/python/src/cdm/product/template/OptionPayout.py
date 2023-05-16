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

__all__ = ['OptionPayout']

from cdm.product.common.settlement.PayoutBase import PayoutBase

class OptionPayout(PayoutBase):
  """
   The option payout specification terms. The associated globalKey denotes the ability to associate a hash value to the respective OptionPayout instantiation for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.
  """
  buyerSeller: BuyerSeller = Field(..., description="")
  exerciseTerms: OptionExercise = Field(..., description="The terms for exercising the option, which include the option style (e.g. American style option), the exercise procedure (e.g. manual exercise) and the settlement terms (e.g. physical vs. cash).")
  """
  The terms for exercising the option, which include the option style (e.g. American style option), the exercise procedure (e.g. manual exercise) and the settlement terms (e.g. physical vs. cash).
  """
  feature: Optional[OptionFeature] = Field(None, description="The option feature, such as quanto, Asian, barrier, knock.")
  """
  The option feature, such as quanto, Asian, barrier, knock.
  """
  observationTerms: Optional[ObservationTerms] = Field(None, description="Class containing terms that are associated with observing a price/benchmark/index across either single or multple observations. To be used for option contracts that reference a benchmark price.")
  """
  Class containing terms that are associated with observing a price/benchmark/index across either single or multple observations. To be used for option contracts that reference a benchmark price.
  """
  optionType: Optional[OptionTypeEnum] = Field(None, description="The type of option transaction. From a usage standpoint, put/call is the default option type, while payer/receiver indicator is used for options on index credit default swaps, consistently with the industry practice. Straddle is used for the case of straddle strategy, that combine a call and a put with the same strike.")
  """
  The type of option transaction. From a usage standpoint, put/call is the default option type, while payer/receiver indicator is used for options on index credit default swaps, consistently with the industry practice. Straddle is used for the case of straddle strategy, that combine a call and a put with the same strike.
  """
  schedule: Optional[CommoditySchedule] = Field(None, description="Allows the full representation of a commodity payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.")
  """
  Allows the full representation of a commodity payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.
  """
  underlier: Product = Field(..., description="The product underlying the option, which can be of any type including ContractualProduct or Security.")
  """
  The product underlying the option, which can be of any type including ContractualProduct or Security.
  """
  
  @rosetta_condition
  def condition_0_ClearedPhysicalSettlementExists(self):
    def _then_fn0():
      return ((self.settlementTerms.physicalSettlementTerms.clearedPhysicalSettlement) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((((self.settlementTerms.physicalSettlementTerms) is not None) and self.check_one_of_constraint(self, self.underlier.contractualProduct.economicTerms.payout.interestRatePayout)) and all_elements(len(self.underlier.contractualProduct.economicTerms.payout.interestRatePayout), "=", 2)), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.BuyerSeller import BuyerSeller
from cdm.product.template.OptionExercise import OptionExercise
from cdm.product.template.OptionFeature import OptionFeature
from cdm.product.common.schedule.ObservationTerms import ObservationTerms
from cdm.product.template.OptionTypeEnum import OptionTypeEnum
from cdm.product.template.CommoditySchedule import CommoditySchedule
from cdm.product.template.Product import Product

OptionPayout.update_forward_refs()
