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

__all__ = ['BondChoiceModel']


class BondChoiceModel(BaseDataClass):
  """
   Either a bond or convertible bond.
  """
  bond: Optional[Bond] = Field(None, description="")
  convertibleBond: Optional[ConvertibleBond] = Field(None, description="")
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('bond', 'convertibleBond', necessity=True)

from cdm.base.staticdata.asset.common.Bond import Bond
from cdm.base.staticdata.asset.common.ConvertibleBond import ConvertibleBond

BondChoiceModel.update_forward_refs()
