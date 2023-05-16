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

__all__ = ['EligibleCollateralCriteria']

from cdm.legaldocumentation.csa.CollateralCriteriaBase import CollateralCriteriaBase

class EligibleCollateralCriteria(CollateralCriteriaBase):
  """
  Represents a set of criteria used to specify eligible collateral.
  """
  treatment: CollateralTreatment = Field(..., description="Identifies the treatment of specified collateral, e.g., haircuts,holding limits or exclusions.")
  """
  Identifies the treatment of specified collateral, e.g., haircuts,holding limits or exclusions.
  """
  
  @rosetta_condition
  def condition_0_ConcentrationLimitTypeIssueOSAmountDebtOnly(self):
    """
    Specifies a condition that concentration limit type 'IssueOutstandingAmount' is restricted to be used only if the asset type is described as 'Security' and 'Debt'.
    """
    def _then_fn0():
      return (all_elements(self.asset.collateralAssetType.securityType, "=", SecurityTypeEnum.DEBT) or all_elements(self.treatment.concentrationLimit.concentrationLimitCriteria.asset.collateralAssetType.securityType, "=", SecurityTypeEnum.DEBT))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements((self.treatment.concentrationLimit.concentrationLimitCriteria.concentrationLimitType), "=", ConcentrationLimitTypeEnum.ISSUE_OUTSTANDING_AMOUNT), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_ConcentrationLimitTypeMarketCapEquityOnly(self):
    """
    Specifies a condition that concentration limit type 'MarketCapitalisation' is restricted to be used only if the asset type is described as 'Security' and 'Equity'.
    """
    def _then_fn0():
      return (all_elements(self.asset.collateralAssetType.securityType, "=", SecurityTypeEnum.EQUITY) or all_elements(self.treatment.concentrationLimit.concentrationLimitCriteria.asset.collateralAssetType.securityType, "=", SecurityTypeEnum.EQUITY))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements((self.treatment.concentrationLimit.concentrationLimitCriteria.concentrationLimitType), "=", ConcentrationLimitTypeEnum.MARKET_CAPITALISATION), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_AverageTradingVolumeEquityOnly(self):
    """
    Specifies a condition that concentration limit 'AverageTradingVolume' is restricted to be used only if the asset type is described as 'Security' and 'Equity'.
    """
    def _then_fn0():
      return (all_elements(self.asset.collateralAssetType.securityType, "=", SecurityTypeEnum.EQUITY) or all_elements(self.treatment.concentrationLimit.concentrationLimitCriteria.asset.collateralAssetType.securityType, "=", SecurityTypeEnum.EQUITY))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.treatment.concentrationLimit.concentrationLimitCriteria.averageTradingVolume) is not None), _then_fn0, _else_fn0)

from cdm.legaldocumentation.csa.CollateralTreatment import CollateralTreatment
from cdm.legaldocumentation.csa.ConcentrationLimitTypeEnum import ConcentrationLimitTypeEnum
from cdm.base.staticdata.asset.common.SecurityTypeEnum import SecurityTypeEnum

EligibleCollateralCriteria.update_forward_refs()
