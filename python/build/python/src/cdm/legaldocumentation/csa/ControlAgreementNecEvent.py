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

__all__ = ['ControlAgreementNecEvent']


class ControlAgreementNecEvent(BaseDataClass):
  """
  A class to specify Control Agreement language related to delivery of a Notice of Exclusive Control
  """
  controlAgreementNecEventElection: List[ControlAgreementNecEventElection] = Field([], description="")
  @rosetta_condition
  def cardinality_controlAgreementNecEventElection(self):
    return check_cardinality(self.controlAgreementNecEventElection, 2, 2)
  

from cdm.legaldocumentation.csa.ControlAgreementNecEventElection import ControlAgreementNecEventElection

ControlAgreementNecEvent.update_forward_refs()
