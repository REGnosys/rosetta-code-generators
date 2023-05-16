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

__all__ = ['BondEquityModel']


class BondEquityModel(BaseDataClass):
  """
   Bond equity model to value convertible bonds and modelled onto BondEquity.model in FpML.
  """
  bondchoiceModel: Optional[BondChoiceModel] = Field(None, description="Either the bond or convertible bond.")
  """
  Either the bond or convertible bond.
  """
  equity: Optional[Equity] = Field(None, description="The equity.")
  """
  The equity.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('bondchoiceModel', 'equity', necessity=True)

from cdm.observable.asset.BondChoiceModel import BondChoiceModel
from cdm.base.staticdata.asset.common.Equity import Equity

BondEquityModel.update_forward_refs()
