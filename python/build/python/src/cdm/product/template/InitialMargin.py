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

__all__ = ['InitialMargin']


class InitialMargin(BaseDataClass):
  """
   Defines initial margin applied to a repo transaction. Initial margin is an agreed premium to the Purchase Price of a repo to determine the required Market Value of the collateral to be delivered on the Purchase Date. It reflects quality of the collateral. Its aim is to calculate the risk-adjusted or liquidation value of collateral.
  """
  margin: List[InitialMarginCalculation] = Field([], description="Initial margin calculation for a collateral asset. Initial margin requirements may be specified for multiple pieces of collateral.")
  """
  Initial margin calculation for a collateral asset. Initial margin requirements may be specified for multiple pieces of collateral.
  """
  @rosetta_condition
  def cardinality_margin(self):
    return check_cardinality(self.margin, 1, None)
  
  marginThreshold: Optional[Money] = Field(None, description="An element defining a margin threshold which is the Net Exposure of a trade below which parties agree they will not call a margin from each other.")
  """
  An element defining a margin threshold which is the Net Exposure of a trade below which parties agree they will not call a margin from each other.
  """
  marginType: MarginTypeEnum = Field(..., description="An element defining the type of assets (cash or securities) specified to apply as margin to the repo transaction. See GMRA 2011 paragraph 2(h) for 'Cash Margin' and GMRA 2011 paragraph 2(cc) for 'Margin Securities'.")
  """
  An element defining the type of assets (cash or securities) specified to apply as margin to the repo transaction. See GMRA 2011 paragraph 2(h) for 'Cash Margin' and GMRA 2011 paragraph 2(cc) for 'Margin Securities'.
  """
  minimumTransferAmount: Optional[Money] = Field(None, description="An element defining a minimum transfer amount which is the minimum margin call parties will make once the margin threshold (or margin ratio threshold / haircut threshold) has been exceeded.")
  """
  An element defining a minimum transfer amount which is the minimum margin call parties will make once the margin threshold (or margin ratio threshold / haircut threshold) has been exceeded.
  """
  
  @rosetta_condition
  def condition_0_MarginThreshold(self):
    def _then_fn0():
      return all_elements(self.marginThreshold.value, ">", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.marginThreshold) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_MinimumTransferAmount(self):
    def _then_fn0():
      return all_elements(self.minimumTransferAmount.value, ">", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.minimumTransferAmount) is not None), _then_fn0, _else_fn0)

from cdm.product.template.InitialMarginCalculation import InitialMarginCalculation
from cdm.observable.asset.Money import Money
from cdm.product.template.MarginTypeEnum import MarginTypeEnum

InitialMargin.update_forward_refs()
