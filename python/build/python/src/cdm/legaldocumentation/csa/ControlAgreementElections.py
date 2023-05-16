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

__all__ = ['ControlAgreementElections']


class ControlAgreementElections(BaseDataClass):
  """
  A class to specify the Control Agreement election sby each party to the agreement.
  """
  consistencyWithControlAgreement: Optional[bool] = Field(None, description="Unless specified as inapplicable in the event of any inconsistency between this Deed and the Control Agreement, this Deed will prevail over the Control Agreement")
  """
  Unless specified as inapplicable in the event of any inconsistency between this Deed and the Control Agreement, this Deed will prevail over the Control Agreement
  """
  controlAgreementAsCsd: bool = Field(..., description="The identification of whether the Control Agreement is a Credit Support Document with respect to each party")
  """
  The identification of whether the Control Agreement is a Credit Support Document with respect to each party
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  relationshipWithControlAgreement: Optional[bool] = Field(None, description="Unless specified as inapplicable the parties recognise that the Control Agreement is a means by which the parties can perform their obligations.")
  """
  Unless specified as inapplicable the parties recognise that the Control Agreement is a means by which the parties can perform their obligations.
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

ControlAgreementElections.update_forward_refs()
