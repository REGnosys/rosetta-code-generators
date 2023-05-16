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

__all__ = ['AssetType']


class AssetType(BaseDataClass):
  """
  Represents a class to allow specification of the asset product type.
  """
  assetType: AssetTypeEnum = Field(..., description="Represents a filter based on the type of collateral asset.")
  """
  Represents a filter based on the type of collateral asset.
  """
  debtType: Optional[DebtType] = Field(None, description="Represents a filter based on the type of bond.")
  """
  Represents a filter based on the type of bond.
  """
  equityType: Optional[EquityTypeEnum] = Field(None, description="Represents a filter based on the type of equity.")
  """
  Represents a filter based on the type of equity.
  """
  fundType: Optional[FundProductTypeEnum] = Field(None, description="Represents a filter based on the type of fund.")
  """
  Represents a filter based on the type of fund.
  """
  otherAssetType: List[str] = Field([], description="Specifies the eligible asset type when not enumerated.")
  """
  Specifies the eligible asset type when not enumerated.
  """
  securityType: Optional[SecurityTypeEnum] = Field(None, description="Represents a filter based on the type of security.")
  """
  Represents a filter based on the type of security.
  """
  
  @rosetta_condition
  def condition_0_SecuritySubType(self):
    def _then_fn0():
      return ((((self.securityType) is None) and ((self.debtType) is None)) and ((self.equityType) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.assetType, "<>", AssetTypeEnum.SECURITY), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_BondSubType(self):
    def _then_fn0():
      return ((self.debtType) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.securityType, "<>", SecurityTypeEnum.DEBT), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_EquitySubType(self):
    def _then_fn0():
      return ((self.equityType) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.securityType, "<>", SecurityTypeEnum.EQUITY), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_FundSubType(self):
    def _then_fn0():
      return ((self.fundType) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.securityType, "<>", SecurityTypeEnum.FUND), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_OtherAssetSubType(self):
    def _then_fn0():
      return ((self.otherAssetType) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.assetType, "=", AssetTypeEnum.OTHER), _then_fn0, _else_fn0)

from cdm.base.staticdata.asset.common.AssetTypeEnum import AssetTypeEnum
from cdm.base.staticdata.asset.common.DebtType import DebtType
from cdm.base.staticdata.asset.common.EquityTypeEnum import EquityTypeEnum
from cdm.base.staticdata.asset.common.FundProductTypeEnum import FundProductTypeEnum
from cdm.base.staticdata.asset.common.SecurityTypeEnum import SecurityTypeEnum

AssetType.update_forward_refs()
