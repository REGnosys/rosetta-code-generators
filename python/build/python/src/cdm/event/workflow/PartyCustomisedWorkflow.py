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

__all__ = ['PartyCustomisedWorkflow']


class PartyCustomisedWorkflow(BaseDataClass):
  """
  A class to specify a party-related, non-standardized data in a generic form.
  """
  customisedWorkflow: List[CustomisedWorkflow] = Field([], description="Non-standardized data in a generic form.")
  """
  Non-standardized data in a generic form.
  """
  @rosetta_condition
  def cardinality_customisedWorkflow(self):
    return check_cardinality(self.customisedWorkflow, 1, None)
  
  partyName: Optional[str] = Field(None, description="The party name to which the workflow pertains to.")
  """
  The party name to which the workflow pertains to.
  """
  partyReference: Optional[AttributeWithReference | Party] = Field(None, description="Reference to the party to which the workflow pertains to.")
  """
  Reference to the party to which the workflow pertains to.
  """
  
  @rosetta_condition
  def condition_0_PartyCustomisedWorkflowChoice(self):
    """
    The identification of the party to which the PartyCustomisedWorkflow pertains to can be done through either a party reference or the party name.
    """
    return self.check_one_of_constraint('partyName', 'partyReference', necessity=True)

from cdm.event.workflow.CustomisedWorkflow import CustomisedWorkflow
from cdm.base.staticdata.party.Party import Party

PartyCustomisedWorkflow.update_forward_refs()
