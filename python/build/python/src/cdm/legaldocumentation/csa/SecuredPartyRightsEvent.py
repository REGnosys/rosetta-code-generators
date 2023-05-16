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

__all__ = ['SecuredPartyRightsEvent']


class SecuredPartyRightsEvent(BaseDataClass):
  """
  A class to specify Secured Party Rights Event language
  """
  earlyTerminationDateOptionalLanguage: bool = Field(..., description="A boolean attribute to specify whether Failure to Pay Early Termination language is included (True) or excluded (False) from the agreement.")
  """
  A boolean attribute to specify whether Failure to Pay Early Termination language is included (True) or excluded (False) from the agreement.
  """
  failureToPayEarlyTermination: Optional[bool] = Field(None, description="A boolean attribute to specify whether Failure to Pay Early Termination language in the agreement is deemed applicable or not.")
  """
  A boolean attribute to specify whether Failure to Pay Early Termination language in the agreement is deemed applicable or not.
  """
  securedPartyRightsEventElection: List[SecuredPartyRightsEventElection] = Field([], description="")
  @rosetta_condition
  def cardinality_securedPartyRightsEventElection(self):
    return check_cardinality(self.securedPartyRightsEventElection, 0, 2)
  
  
  @rosetta_condition
  def condition_0_FailureToPayLanguage(self):
    """
    A data rule to enforce that the applicability of Failure to Pay language is only applied when Early Termination language is included.
    """
    def _then_fn0():
      return ((self.failureToPayEarlyTermination) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.earlyTerminationDateOptionalLanguage, "=", False), _then_fn0, _else_fn0)

from cdm.legaldocumentation.csa.SecuredPartyRightsEventElection import SecuredPartyRightsEventElection

SecuredPartyRightsEvent.update_forward_refs()
