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

__all__ = ['TransferBase']


class TransferBase(BaseDataClass):
  identifier: List[AttributeWithMeta[Identifier] | Identifier] = Field([], description="Represents a unique reference to the transfer.")
  """
  Represents a unique reference to the transfer.
  """
  observable: Optional[Observable] = Field(None, description="Represents the object that is subject to the transfer, it could be an asset or a reference.")
  """
  Represents the object that is subject to the transfer, it could be an asset or a reference.
  """
  payerReceiver: PartyReferencePayerReceiver = Field(..., description="Represents the parties to the transfer and their role.")
  """
  Represents the parties to the transfer and their role.
  """
  quantity: Quantity = Field(..., description="Represents the amount of the asset to be transferred.")
  """
  Represents the amount of the asset to be transferred.
  """
  settlementDate: AdjustableOrAdjustedOrRelativeDate = Field(..., description="Represents the date on which the transfer to due.")
  """
  Represents the date on which the transfer to due.
  """
  
  @rosetta_condition
  def condition_0_FinancialUnitExists(self):
    def _then_fn0():
      return ((self.quantity.unit.financialUnit) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.observable) is not None), _then_fn0, _else_fn0)

from cdm.base.staticdata.identifier.Identifier import Identifier
from cdm.observable.asset.Observable import Observable
from cdm.base.staticdata.party.PartyReferencePayerReceiver import PartyReferencePayerReceiver
from cdm.base.math.Quantity import Quantity
from cdm.base.datetime.AdjustableOrAdjustedOrRelativeDate import AdjustableOrAdjustedOrRelativeDate

TransferBase.update_forward_refs()
