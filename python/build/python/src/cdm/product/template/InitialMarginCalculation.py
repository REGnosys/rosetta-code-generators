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

__all__ = ['InitialMarginCalculation']


class InitialMarginCalculation(BaseDataClass):
  """
   Defines the initial margin calculation applicable to a single piece of collateral.
  """
  haircut: Optional[Decimal] = Field(None, description="An element defining a haircut expressed as the percentage difference between the Market Value of the collateral and the Purchase Price of the repo and calculated as 100 multiplied by a ratio of the difference between the Market Value of the collateral and the Purchase Price of the repo to the Market Value of the collateral. Haircut is alternative way to adjust the value of collateral sold in a repurchase agreement to initial margin ratio. Because an initial margin is a percentage of the Purchase Price, while a haircut is a percentage of the Market Value of collateral, the arithmetic of initial margins and haircuts is slightly different. For example, an initial margin of 102% is not equivalent to a haircut of 2%, but to 1.961% (ie 100/102%). See GMRA 2011 paragraph 2(aa).")
  """
  An element defining a haircut expressed as the percentage difference between the Market Value of the collateral and the Purchase Price of the repo and calculated as 100 multiplied by a ratio of the difference between the Market Value of the collateral and the Purchase Price of the repo to the Market Value of the collateral. Haircut is alternative way to adjust the value of collateral sold in a repurchase agreement to initial margin ratio. Because an initial margin is a percentage of the Purchase Price, while a haircut is a percentage of the Market Value of collateral, the arithmetic of initial margins and haircuts is slightly different. For example, an initial margin of 102% is not equivalent to a haircut of 2%, but to 1.961% (ie 100/102%). See GMRA 2011 paragraph 2(aa).
  """
  haircutThreshold: List[Decimal] = Field([], description="An element defining a haircut percentage threshold which is the value above (when it's lower than initial haircut) or below (when it's higher than initial haircut) which parties agree they will not call a margin from each other.")
  """
  An element defining a haircut percentage threshold which is the value above (when it's lower than initial haircut) or below (when it's higher than initial haircut) which parties agree they will not call a margin from each other.
  """
  @rosetta_condition
  def cardinality_haircutThreshold(self):
    return check_cardinality(self.haircutThreshold, 0, 2)
  
  marginRatio: Optional[Decimal] = Field(None, description="An element defining an initial margin expressed as a ratio of the Market Value of the collateral to the Purchase Price. A default value of initial margin ratio of 1.00 means there is no margin and thus no risk related with the collateral. See GMRA 2000 paragraph 2(z) and GMRA 2011 paragraph 2(bb).")
  """
  An element defining an initial margin expressed as a ratio of the Market Value of the collateral to the Purchase Price. A default value of initial margin ratio of 1.00 means there is no margin and thus no risk related with the collateral. See GMRA 2000 paragraph 2(z) and GMRA 2011 paragraph 2(bb).
  """
  marginRatioThreshold: List[Decimal] = Field([], description="An element defining a margin ratio threshold which is the value above (when it's lower than initial margin ratio) or below (when it's higher than initial margin ratio) which parties agree they will not call a margin from each other.")
  """
  An element defining a margin ratio threshold which is the value above (when it's lower than initial margin ratio) or below (when it's higher than initial margin ratio) which parties agree they will not call a margin from each other.
  """
  @rosetta_condition
  def cardinality_marginRatioThreshold(self):
    return check_cardinality(self.marginRatioThreshold, 0, 2)
  
  
  @rosetta_condition
  def condition_0_InitialMarginCalculationChoice(self):
    return self.check_one_of_constraint('marginRatio', 'haircut', necessity=True)


InitialMarginCalculation.update_forward_refs()
