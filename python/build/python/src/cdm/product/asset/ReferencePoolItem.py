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

__all__ = ['ReferencePoolItem']


class ReferencePoolItem(BaseDataClass):
  """
  This type contains all the constituent weight and reference information.
  """
  cashSettlementTermsReference: Optional[AttributeWithReference | CashSettlementTerms] = Field(None, description="Reference to the cash settlement terms applicable to this item.")
  """
  Reference to the cash settlement terms applicable to this item.
  """
  constituentWeight: Optional[ConstituentWeight] = Field(None, description="Describes the weight of each of the constituents within the basket. If not provided, it is assumed to be equal weighted.")
  """
  Describes the weight of each of the constituents within the basket. If not provided, it is assumed to be equal weighted.
  """
  physicalSettlementTermsReference: Optional[AttributeWithReference | PhysicalSettlementTerms] = Field(None, description="Reference to the physical settlement terms applicable to this item.")
  """
  Reference to the physical settlement terms applicable to this item.
  """
  protectionTermsReference: Optional[AttributeWithReference | ProtectionTerms] = Field(None, description="Reference to the documentation terms applicable to this item.")
  """
  Reference to the documentation terms applicable to this item.
  """
  referencePair: ReferencePair = Field(..., description="")
  
  @rosetta_condition
  def condition_0_SettlementChoice(self):
    """
    A choice rule between a reference to the cash or physical settlement terms.
    """
    return self.check_one_of_constraint('cashSettlementTermsReference', 'physicalSettlementTermsReference', necessity=False)

from cdm.product.common.settlement.CashSettlementTerms import CashSettlementTerms
from cdm.product.template.ConstituentWeight import ConstituentWeight
from cdm.product.common.settlement.PhysicalSettlementTerms import PhysicalSettlementTerms
from cdm.product.asset.ProtectionTerms import ProtectionTerms
from cdm.product.asset.ReferencePair import ReferencePair

ReferencePoolItem.update_forward_refs()
