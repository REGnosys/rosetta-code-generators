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

__all__ = ['Workflow']


class Workflow(BaseDataClass):
  """
  A collection of workflow steps which together makeup an entire workflow sequence.
  """
  steps: List[WorkflowStep] = Field([], description="")
  @rosetta_condition
  def cardinality_steps(self):
    return check_cardinality(self.steps, 1, None)
  

from cdm.event.workflow.WorkflowStep import WorkflowStep

Workflow.update_forward_refs()
