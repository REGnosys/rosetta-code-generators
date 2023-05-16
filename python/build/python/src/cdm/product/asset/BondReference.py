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

__all__ = ['BondReference']


class BondReference(BaseDataClass):
  """
  Reference to a bond underlier to represent an asset swap or Condition Precedent Bond.
  """
  bond: ProductIdentifier = Field(..., description="Reference to a bond underlier.")
  """
  Reference to a bond underlier.
  """
  conditionPrecedentBond: bool = Field(..., description="To indicate whether the Condition Precedent Bond is applicable. The swap contract is only valid if the bond is issued and if there is any dispute over the terms of fixed stream then the bond terms would be used.")
  """
  To indicate whether the Condition Precedent Bond is applicable. The swap contract is only valid if the bond is issued and if there is any dispute over the terms of fixed stream then the bond terms would be used.
  """
  discrepancyClause: Optional[bool] = Field(None, description="To indicate whether the Discrepancy Clause is applicable.")
  """
  To indicate whether the Discrepancy Clause is applicable.
  """

from cdm.base.staticdata.asset.common.ProductIdentifier import ProductIdentifier

BondReference.update_forward_refs()
