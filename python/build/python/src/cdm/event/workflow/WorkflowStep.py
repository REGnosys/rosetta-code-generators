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

__all__ = ['WorkflowStep']


class WorkflowStep(BaseDataClass):
  """
  A workflow step represents the state of a business event. The workflow step contains a reference to a previous WorkflowStep in order to preserve lineage. A workflow step is accepted if it contains a business event, proposed if proposedEvent is present and is rejected if the rejected flag is set.
  """
  account: List[Account] = Field([], description="Optional account information that could be associated to the event.")
  """
  Optional account information that could be associated to the event.
  """
  action: Optional[ActionEnum] = Field(None, description="Specifies whether the event is a new, a correction or a cancellation.")
  """
  Specifies whether the event is a new, a correction or a cancellation.
  """
  businessEvent: Optional[BusinessEvent] = Field(None, description="Life cycle event for the step. The businessEvent is optional when a proposedEvent or rejection are present.")
  """
  Life cycle event for the step. The businessEvent is optional when a proposedEvent or rejection are present.
  """
  creditLimitInformation: Optional[CreditLimitInformation] = Field(None, description="")
  eventIdentifier: List[Identifier] = Field([], description="The identifier(s) that uniquely identify a lifecycle event. The unbounded cardinality is meant to provide the ability to associate identifiers that are issued by distinct parties. As an example, each of the parties to the event may choose to associate their own identifiers to the event.")
  """
  The identifier(s) that uniquely identify a lifecycle event. The unbounded cardinality is meant to provide the ability to associate identifiers that are issued by distinct parties. As an example, each of the parties to the event may choose to associate their own identifiers to the event.
  """
  @rosetta_condition
  def cardinality_eventIdentifier(self):
    return check_cardinality(self.eventIdentifier, 1, None)
  
  lineage: Optional[Lineage] = Field(None, description="The lineage attribute provides a linkage among lifecycle events through the globalKey hash value. One example is when a given lifecycle event is being corrected or cancelled. In such case, each subsequent event will have lineage into the prior version of that event. The second broad use case is when an event has a dependency upon either another event (e.g. the regular payment associated with a fix/float swap will have a lineage into the reset event, which will in turn have a lineage into the observation event for the floating rate and the contract) or a contract (e.g. the exercise of an option has a lineage into that option).")
  """
  The lineage attribute provides a linkage among lifecycle events through the globalKey hash value. One example is when a given lifecycle event is being corrected or cancelled. In such case, each subsequent event will have lineage into the prior version of that event. The second broad use case is when an event has a dependency upon either another event (e.g. the regular payment associated with a fix/float swap will have a lineage into the reset event, which will in turn have a lineage into the observation event for the floating rate and the contract) or a contract (e.g. the exercise of an option has a lineage into that option).
  """
  messageInformation: Optional[MessageInformation] = Field(None, description="Contains all information pertaining the FpML messaging header ")
  """
  Contains all information pertaining the FpML messaging header 
  """
  nextEvent: Optional[EventInstruction] = Field(None, description="The intended next event can be specified, even if the instructions are not known yet.")
  """
  The intended next event can be specified, even if the instructions are not known yet.
  """
  party: List[Party] = Field([], description="The specification of the event parties. This attribute is optional, as not applicable to certain events (e.g. most of the observations).")
  """
  The specification of the event parties. This attribute is optional, as not applicable to certain events (e.g. most of the observations).
  """
  previousWorkflowStep: Optional[AttributeWithReference | WorkflowStep] = Field(None, description="Optional previous workflow step that provides lineage to workflow steps that precedes it.")
  """
  Optional previous workflow step that provides lineage to workflow steps that precedes it.
  """
  proposedEvent: Optional[EventInstruction] = Field(None, description="The proposed event for a workflow step. The proposedEvent is optional when the businessEvent or rejection are present")
  """
  The proposed event for a workflow step. The proposedEvent is optional when the businessEvent or rejection are present
  """
  rejected: Optional[bool] = Field(None, description="Flags this step as rejected.")
  """
  Flags this step as rejected.
  """
  timestamp: List[EventTimestamp] = Field([], description="The set of timestamp(s) associated with the event as a collection of [dateTime, qualifier].")
  """
  The set of timestamp(s) associated with the event as a collection of [dateTime, qualifier].
  """
  @rosetta_condition
  def cardinality_timestamp(self):
    return check_cardinality(self.timestamp, 1, None)
  
  workflowState: Optional[WorkflowState] = Field(None, description="The event workflow information, i.e. the workflow status, the associated comment and the partyCustomisedWorkflow which purpose is to provide the ability to associate custom workflow information to the CDM.")
  """
  The event workflow information, i.e. the workflow status, the associated comment and the partyCustomisedWorkflow which purpose is to provide the ability to associate custom workflow information to the CDM.
  """
  
  @rosetta_condition
  def condition_0_WorkflowStepStatus(self):
    return ((((((((WorkflowStep.businessEvent) is not None) and ((WorkflowStep.nextEvent.instruction) is None)) and ((WorkflowStep.rejected) is None)) or ((((WorkflowStep.nextEvent.instruction) is not None) and ((WorkflowStep.businessEvent) is None)) and ((WorkflowStep.rejected) is None))) or ((((WorkflowStep.rejected) is not None) and ((WorkflowStep.businessEvent) is None)) and ((WorkflowStep.nextEvent) is None))) or ((((WorkflowStep.proposedEvent) is not None) and ((WorkflowStep.nextEvent) is None)) and ((WorkflowStep.rejected) is None))) or (((WorkflowStep.previousWorkflowStep) is not None) and all_elements(self.action, "=", ActionEnum.CANCEL)))

from cdm.base.staticdata.party.Account import Account
from cdm.event.common.ActionEnum import ActionEnum
from cdm.event.common.BusinessEvent import BusinessEvent
from cdm.event.workflow.CreditLimitInformation import CreditLimitInformation
from cdm.base.staticdata.identifier.Identifier import Identifier
from cdm.event.common.Lineage import Lineage
from cdm.event.workflow.MessageInformation import MessageInformation
from cdm.event.workflow.EventInstruction import EventInstruction
from cdm.base.staticdata.party.Party import Party
from cdm.event.workflow.WorkflowStep import WorkflowStep
from cdm.event.workflow.EventTimestamp import EventTimestamp
from cdm.event.workflow.WorkflowState import WorkflowState

WorkflowStep.update_forward_refs()
