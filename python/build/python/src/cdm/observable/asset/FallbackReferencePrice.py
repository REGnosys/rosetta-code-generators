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

__all__ = ['FallbackReferencePrice']


class FallbackReferencePrice(BaseDataClass):
  """
  The method, prioritised by the order it is listed in this element, to get a replacement rate for the disrupted settlement rate option.
  """
  calculationAgentDetermination: Optional[CalculationAgent] = Field(None, description="The calculation agent will decide the rate.")
  """
  The calculation agent will decide the rate.
  """
  fallBackSettlementRateOption: List[AttributeWithMeta[SettlementRateOptionEnum] | SettlementRateOptionEnum] = Field([], description="This settlement rate option will be used in its place.")
  """
  This settlement rate option will be used in its place.
  """
  fallbackSurveyValuationPostponement: Optional[bool] = Field(None, description="Request rate quotes from the market. This element is set as type Empty in FpML. When present, the FpML synonym is mapped to a value True in the CDM.")
  """
  Request rate quotes from the market. This element is set as type Empty in FpML. When present, the FpML synonym is mapped to a value True in the CDM.
  """
  valuationPostponement: Optional[ValuationPostponement] = Field(None, description="Specifies how long to wait to get a quote from a settlement rate option upon a price source disruption.")
  """
  Specifies how long to wait to get a quote from a settlement rate option upon a price source disruption.
  """
  
  @rosetta_condition
  def condition_0_MaximumDaysOfPostponement(self):
    """
    FpML specifies maximumDaysOfPostponement as a positive integer.
    """
    def _then_fn0():
      return all_elements(self.valuationPostponement.maximumDaysOfPostponement, ">", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.valuationPostponement) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_FallbackCalculationAgent(self):
    def _then_fn0():
      return all_elements(self.calculationAgentDetermination.calculationAgentParty, "=", AncillaryRoleEnum.CALCULATION_AGENT_FALLBACK)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.calculationAgentDetermination.calculationAgentParty) is not None), _then_fn0, _else_fn0)

from cdm.observable.asset.CalculationAgent import CalculationAgent
from cdm.observable.asset.SettlementRateOptionEnum import SettlementRateOptionEnum
from cdm.observable.asset.ValuationPostponement import ValuationPostponement
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

FallbackReferencePrice.update_forward_refs()
