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

__all__ = ['CollateralValuationTreatment']


class CollateralValuationTreatment(BaseDataClass):
  """
  Specification of the valuation treatment for the specified collateral.
  """
  additionalHaircutPercentage: Optional[Decimal] = Field(None, description="Specifies a percentage value of any additional haircut to be applied to a collateral asset,the percentage value is expressed as the discount haircut to the value of the collateral- as an example a 5% haircut would be expressed as 0.05. ")
  """
  Specifies a percentage value of any additional haircut to be applied to a collateral asset,the percentage value is expressed as the discount haircut to the value of the collateral- as an example a 5% haircut would be expressed as 0.05. 
  """
  fxHaircutPercentage: Optional[Decimal] = Field(None, description="Specifies an FX haircut applied to a specific asset which is agreed between the parties (for example, if pledgor eligible collateral is not denominated in the termination currency or under other specified cases in collateral support documents both for initial margin and variation margin).The percentage value is expressed as the discount haircut to the value of the collateral- as an example an 8% FX haircut would be expressed as 0.08.")
  """
  Specifies an FX haircut applied to a specific asset which is agreed between the parties (for example, if pledgor eligible collateral is not denominated in the termination currency or under other specified cases in collateral support documents both for initial margin and variation margin).The percentage value is expressed as the discount haircut to the value of the collateral- as an example an 8% FX haircut would be expressed as 0.08.
  """
  haircutPercentage: Optional[Decimal] = Field(None, description="Specifies a haircut percentage to be applied to the value of asset and used as a discount factor to the value of the collateral asset,expressed as a percentage in decimal terms. As an example a 0.5% haircut would be represented as a decimal number 0.005.")
  """
  Specifies a haircut percentage to be applied to the value of asset and used as a discount factor to the value of the collateral asset,expressed as a percentage in decimal terms. As an example a 0.5% haircut would be represented as a decimal number 0.005.
  """
  marginPercentage: Optional[Decimal] = Field(None, description="Specifies a percentage value of transaction needing to be posted as collateral expressed as a valuation. As an example a 104% requirement would be represented as a decimal number 1.04.")
  """
  Specifies a percentage value of transaction needing to be posted as collateral expressed as a valuation. As an example a 104% requirement would be represented as a decimal number 1.04.
  """
  
  @rosetta_condition
  def condition_0_HaircutPercentage(self):
    """
    A data rule to validate that if a Valuation Percentage is specified it should be greater than or equal to 0 and less than 1.
    """
    def _then_fn0():
      return (all_elements(self.haircutPercentage, ">=", 0) and all_elements(self.haircutPercentage, "<", 1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.haircutPercentage) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_MarginPercentage(self):
    """
    A data rule to validate that if a Margin Percentage is specified it should be greater than 1.
    """
    def _then_fn0():
      return all_elements(self.marginPercentage, ">=", 1)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.marginPercentage) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_FxHaircutPercentage(self):
    """
    A data rule to validate that if an FX Haircut Percentage is specified it should be between 0 and less than 1.
    """
    def _then_fn0():
      return (all_elements(self.fxHaircutPercentage, ">", 0) and all_elements(self.fxHaircutPercentage, "<", 1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.fxHaircutPercentage) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_AdditionalHaircutPercentage(self):
    """
    A data rule to validate that if an FX Haircut Percentage is specified it should be between 0 and  less than 1.
    """
    def _then_fn0():
      return (all_elements(self.additionalHaircutPercentage, ">", 0) and all_elements(self.additionalHaircutPercentage, "<", 1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.additionalHaircutPercentage) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_HaircutPercentageOrMarginPercentage(self):
    """
    Choice rule requiring that either a haircut percentage or margin percentage is specified.
    """
    return self.check_one_of_constraint('haircutPercentage', 'marginPercentage', necessity=True)


CollateralValuationTreatment.update_forward_refs()
