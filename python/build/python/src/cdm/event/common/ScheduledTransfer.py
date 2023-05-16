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

__all__ = ['ScheduledTransfer']


class ScheduledTransfer(BaseDataClass):
  corporateActionTransferType: Optional[CorporateActionTypeEnum] = Field(None, description="")
  transferType: ScheduledTransferEnum = Field(..., description="Specifies a transfer created from a scheduled or contingent event on a contract, e.g. Exercise, Performance, Credit Event")
  """
  Specifies a transfer created from a scheduled or contingent event on a contract, e.g. Exercise, Performance, Credit Event
  """
  
  @rosetta_condition
  def condition_0_CorporateActionTransferTypeExists(self):
    """
    When transfer type is Performance or Transfer then the type of event must be specified.
    """
    def _then_fn0():
      return ((self.corporateActionTransferType) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.transferType, "=", ScheduledTransferEnum.CORPORATE_ACTION), _then_fn0, _else_fn0)

from cdm.event.common.CorporateActionTypeEnum import CorporateActionTypeEnum
from cdm.product.common.settlement.ScheduledTransferEnum import ScheduledTransferEnum

ScheduledTransfer.update_forward_refs()
