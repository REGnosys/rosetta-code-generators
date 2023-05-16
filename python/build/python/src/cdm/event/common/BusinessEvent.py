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

__all__ = ['BusinessEvent']


class BusinessEvent(BaseDataClass):
  """
  A business event represents a life cycle event of a trade. The combination of the state changes results in a qualifiable life cycle event. An example of a Business Event is a PartialTermination which is a defined by a quantity change primitive event.
  """
  after: List[TradeState] = Field([], description="Specifies the after trade state(s) created.")
  """
  Specifies the after trade state(s) created.
  """
  corporateActionIntent: Optional[CorporateActionTypeEnum] = Field(None, description="")
  effectiveDate: Optional[date] = Field(None, description="The date on which the event contractually takes effect, when different from the event date.")
  """
  The date on which the event contractually takes effect, when different from the event date.
  """
  eventDate: date = Field(..., description="Specifies the date on which the event is taking place. This date is equal to the trade date in the case of a simple execution.  However it can be different from the trade date, for example in the case of a partial termination.")
  """
  Specifies the date on which the event is taking place. This date is equal to the trade date in the case of a simple execution.  However it can be different from the trade date, for example in the case of a partial termination.
  """
  eventQualifier: Optional[str] = Field(None, description="The CDM event qualifier, which corresponds to the outcome of the isEvent qualification logic which qualifies the lifecycle event as a function of its features (e.g. PartialTermination, ClearingSubmission, Novation, ...).")
  """
  The CDM event qualifier, which corresponds to the outcome of the isEvent qualification logic which qualifies the lifecycle event as a function of its features (e.g. PartialTermination, ClearingSubmission, Novation, ...).
  """
  instruction: List[Instruction] = Field([], description="Specifies the instructions  were used to create the Business Event.")
  """
  Specifies the instructions  were used to create the Business Event.
  """
  intent: Optional[EventIntentEnum] = Field(None, description="The intent attribute is meant to be specified when the event qualification cannot be programmatically inferred from the event features. As a result it is only associated with those primitives that can give way to such ambiguity, the quantityChange being one of those. An example of such is a reduction in the trade notional, which could be interpreted as either a trade correction (unless a maximum period of time post-event is specified as part of the qualification), a partial termination or a portfolio rebalancing in the case of an equity swap. On the other hand, an event such as the exercise is not expected to have an associated intent as there should not be ambiguity.")
  """
  The intent attribute is meant to be specified when the event qualification cannot be programmatically inferred from the event features. As a result it is only associated with those primitives that can give way to such ambiguity, the quantityChange being one of those. An example of such is a reduction in the trade notional, which could be interpreted as either a trade correction (unless a maximum period of time post-event is specified as part of the qualification), a partial termination or a portfolio rebalancing in the case of an equity swap. On the other hand, an event such as the exercise is not expected to have an associated intent as there should not be ambiguity.
  """
  packageInformation: Optional[IdentifiedList] = Field(None, description="Specifies the package information in case the business event represents several trades executed as a package (hence this attribute is optional). The package information is only instantiated once at the business event level to preserve referential integrity, whereas individual trades make reference to it to identify that they are part of a package.")
  """
  Specifies the package information in case the business event represents several trades executed as a package (hence this attribute is optional). The package information is only instantiated once at the business event level to preserve referential integrity, whereas individual trades make reference to it to identify that they are part of a package.
  """
  
  @rosetta_condition
  def condition_0_CorporateAction(self):
    def _then_fn0():
      return all_elements(self.intent, "=", EventIntentEnum.CORPORATE_ACTION_ADJUSTMENT)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.corporateActionIntent) is not None), _then_fn0, _else_fn0)

from cdm.event.common.TradeState import TradeState
from cdm.event.common.CorporateActionTypeEnum import CorporateActionTypeEnum
from cdm.event.common.Instruction import Instruction
from cdm.event.common.EventIntentEnum import EventIntentEnum
from cdm.base.staticdata.identifier.IdentifiedList import IdentifiedList

BusinessEvent.update_forward_refs()
