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

__all__ = ['CollateralIssuerType']


class CollateralIssuerType(BaseDataClass):
  """
  Represents a class to allow specification of the type of entity issuing the collateral.
  """
  issuerType: IssuerTypeEnum = Field(..., description="Specifies the origin of entity issuing the collateral.")
  """
  Specifies the origin of entity issuing the collateral.
  """
  quasiGovernmentType: Optional[QuasiGovernmentIssuerType] = Field(None, description="Specifies debt issues by institutions or bodies, typically constituted by statute, with a function mandated by the government and subject to government supervision inclusive of profit- and non-profit making bodies. Includes the US Agencies and GSEs and the EU concept of public sector entities. Excluding any entities which are also Regional Government.")
  """
  Specifies debt issues by institutions or bodies, typically constituted by statute, with a function mandated by the government and subject to government supervision inclusive of profit- and non-profit making bodies. Includes the US Agencies and GSEs and the EU concept of public sector entities. Excluding any entities which are also Regional Government.
  """
  regionalGovernmentType: Optional[RegionalGovernmentIssuerType] = Field(None, description="Specifies Regional government, local authority or municipal.")
  """
  Specifies Regional government, local authority or municipal.
  """
  specialPurposeVehicleType: Optional[SpecialPurposeVehicleIssuerType] = Field(None, description="Specifies a subsidiary company that is formed to undertake a specific business purpose of acquisition and financing of specific assets on a potentially limited recourse basis dependent of how it is designed. E.g. asset backed securities, including securitisations.")
  """
  Specifies a subsidiary company that is formed to undertake a specific business purpose of acquisition and financing of specific assets on a potentially limited recourse basis dependent of how it is designed. E.g. asset backed securities, including securitisations.
  """
  supraNationalType: Optional[SupraNationalIssuerTypeEnum] = Field(None, description="Specifies debt issued by international organisations and multilateral banks.")
  """
  Specifies debt issued by international organisations and multilateral banks.
  """
  
  @rosetta_condition
  def condition_0_SupraNationalSubType(self):
    def _then_fn0():
      return ((self.supraNationalType) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.issuerType, "<>", IssuerTypeEnum.SUPRA_NATIONAL), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_QuasiGovernmentSubType(self):
    def _then_fn0():
      return ((self.quasiGovernmentType) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.issuerType, "<>", IssuerTypeEnum.QUASI_GOVERNMENT), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_RegionalGovernmentSubType(self):
    def _then_fn0():
      return ((self.regionalGovernmentType) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.issuerType, "<>", IssuerTypeEnum.REGIONAL_GOVERNMENT), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_SpecialPurposeVehicleSubType(self):
    def _then_fn0():
      return ((self.specialPurposeVehicleType) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.issuerType, "<>", IssuerTypeEnum.SPECIAL_PURPOSE_VEHICLE), _then_fn0, _else_fn0)

from cdm.base.staticdata.asset.common.IssuerTypeEnum import IssuerTypeEnum
from cdm.base.staticdata.asset.common.QuasiGovernmentIssuerType import QuasiGovernmentIssuerType
from cdm.base.staticdata.asset.common.RegionalGovernmentIssuerType import RegionalGovernmentIssuerType
from cdm.base.staticdata.asset.common.SpecialPurposeVehicleIssuerType import SpecialPurposeVehicleIssuerType
from cdm.base.staticdata.asset.common.SupraNationalIssuerTypeEnum import SupraNationalIssuerTypeEnum

CollateralIssuerType.update_forward_refs()
