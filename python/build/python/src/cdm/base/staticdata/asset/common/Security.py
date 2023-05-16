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

__all__ = ['Security']

from cdm.base.staticdata.asset.common.ProductBase import ProductBase

class Security(ProductBase):
  """
  Identifies a security by referencing a product identifier and by specifying the sector.
  """
  debtType: Optional[DebtType] = Field(None, description="Identifies the type of debt and selected debt economics.")
  """
  Identifies the type of debt and selected debt economics.
  """
  economicTerms: Optional[EconomicTerms] = Field(None, description="The economic terms associated with a contractual product, i.e. the set of features that are price-forming.")
  """
  The economic terms associated with a contractual product, i.e. the set of features that are price-forming.
  """
  equityType: Optional[EquityTypeEnum] = Field(None, description="Identifies the type of equity.")
  """
  Identifies the type of equity.
  """
  fundType: Optional[FundProductTypeEnum] = Field(None, description="Identifies the type of fund.")
  """
  Identifies the type of fund.
  """
  securityType: SecurityTypeEnum = Field(..., description="Identifies the type of security using an enumerated list.")
  """
  Identifies the type of security using an enumerated list.
  """
  
  @rosetta_condition
  def condition_0_DebtSubType(self):
    def _then_fn0():
      return ((self.debtType) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.securityType, "<>", SecurityTypeEnum.DEBT), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_EquitySubType(self):
    def _then_fn0():
      return ((self.equityType) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.securityType, "<>", SecurityTypeEnum.EQUITY), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_FundSubType(self):
    def _then_fn0():
      return ((self.fundType) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(any_elements(self.securityType, "<>", SecurityTypeEnum.FUND), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_BondEconomicTerms(self):
    def _then_fn0():
      return all_elements(self.securityType, "=", SecurityTypeEnum.DEBT)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.economicTerms) is not None), _then_fn0, _else_fn0)

from cdm.base.staticdata.asset.common.DebtType import DebtType
from cdm.product.template.EconomicTerms import EconomicTerms
from cdm.base.staticdata.asset.common.EquityTypeEnum import EquityTypeEnum
from cdm.base.staticdata.asset.common.FundProductTypeEnum import FundProductTypeEnum
from cdm.base.staticdata.asset.common.SecurityTypeEnum import SecurityTypeEnum

Security.update_forward_refs()
