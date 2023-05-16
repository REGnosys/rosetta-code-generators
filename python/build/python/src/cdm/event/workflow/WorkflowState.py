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

__all__ = ['WorkflowState']


class WorkflowState(BaseDataClass):
  """
  A class to specify workflow information, which is conceptually applicable to all lifecycle events.
  """
  comment: Optional[str] = Field(None, description="A comment field to be associated with the workflow, e.g. to specify why a transaction event was rejected by a party.")
  """
  A comment field to be associated with the workflow, e.g. to specify why a transaction event was rejected by a party.
  """
  partyCustomisedWorkflow: List[PartyCustomisedWorkflow] = Field([], description="Workflow data that is specific to certain market participants and is expressed as part of the CDM in a very generic manner, which can be party-specific. The initial use cases have been derived from the CME clearing and the DTCC TIW submissions.")
  """
  Workflow data that is specific to certain market participants and is expressed as part of the CDM in a very generic manner, which can be party-specific. The initial use cases have been derived from the CME clearing and the DTCC TIW submissions.
  """
  warehouseIdentity: Optional[WarehouseIdentityEnum] = Field(None, description="The identity of the warehouse, if any, that is executing that workflow step.")
  """
  The identity of the warehouse, if any, that is executing that workflow step.
  """
  workflowStatus: WorkflowStatusEnum = Field(..., description="The workflow status indicator, e.g. Accepted, Rejected, ...")
  """
  The workflow status indicator, e.g. Accepted, Rejected, ...
  """

from cdm.event.workflow.PartyCustomisedWorkflow import PartyCustomisedWorkflow
from cdm.event.workflow.WarehouseIdentityEnum import WarehouseIdentityEnum
from cdm.event.workflow.WorkflowStatusEnum import WorkflowStatusEnum

WorkflowState.update_forward_refs()
