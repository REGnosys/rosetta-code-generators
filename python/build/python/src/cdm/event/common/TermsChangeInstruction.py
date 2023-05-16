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

__all__ = ['TermsChangeInstruction']


class TermsChangeInstruction(BaseDataClass):
  """
  Specifies instructions for terms change consisting of the new transaction terms, and the renegotiation fee.
  """
  adjustment: Optional[NotionalAdjustmentEnum] = Field(None, description="")
  ancillaryParty: List[AncillaryParty] = Field([], description="ancillary party to be changed")
  """
  ancillary party to be changed
  """
  product: Optional[Product] = Field(None, description="product to be changed")
  """
  product to be changed
  """
  
  @rosetta_condition
  def condition_0_AtLeastOneOf(self):
    return ((((self.product) is not None) or ((self.ancillaryParty) is not None)) or ((self.adjustment) is not None))

from cdm.product.common.NotionalAdjustmentEnum import NotionalAdjustmentEnum
from cdm.base.staticdata.party.AncillaryParty import AncillaryParty
from cdm.product.template.Product import Product

TermsChangeInstruction.update_forward_refs()
