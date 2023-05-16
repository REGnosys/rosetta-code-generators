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

__all__ = ['SecurityValuationModel']


class SecurityValuationModel(BaseDataClass):
  """
   The security valuation model choice, which can either be based on nominal amount as for a bond, or on the number of contract units as for equity.
  """
  bondValuationModel: Optional[BondValuationModel] = Field(None, description="The valuation model when the security is a bond.")
  """
  The valuation model when the security is a bond.
  """
  unitContractValuationModel: Optional[UnitContractValuationModel] = Field(None, description="The valuation model when the security is a unit contract like equity.")
  """
  The valuation model when the security is a unit contract like equity.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('bondValuationModel', 'unitContractValuationModel', necessity=True)

from cdm.observable.asset.BondValuationModel import BondValuationModel
from cdm.observable.asset.UnitContractValuationModel import UnitContractValuationModel

SecurityValuationModel.update_forward_refs()
