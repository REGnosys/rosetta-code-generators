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

__all__ = ['DeliveryAmount']


class DeliveryAmount(BaseDataClass):
  """
  A class to specify the application of Interest Amount with respect the Delivery Amount. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).
  """
  customElection: Optional[str] = Field(None, description="The custom election that might be specified by the parties to the agreement.")
  """
  The custom election that might be specified by the parties to the agreement.
  """
  standardElection: Optional[DeliveryAmountElectionEnum] = Field(None, description="The standard election as specified by an enumeration.")
  """
  The standard election as specified by an enumeration.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('standardElection', 'customElection', necessity=True)

from cdm.legaldocumentation.csa.DeliveryAmountElectionEnum import DeliveryAmountElectionEnum

DeliveryAmount.update_forward_refs()
