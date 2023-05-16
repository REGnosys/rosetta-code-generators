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

__all__ = ['ConditionsPrecedent']


class ConditionsPrecedent(BaseDataClass):
  """
  A class to specify the two set of elections that may overwrite the default Condition Precedent provision as specified in Paragraph 4, (a) of the ISDA 2016 Credit Support Annex for Initial Margin and the ISDA 2016 Credit Support Annex for Variation Margin. | ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (e): Conditions Precedent. | ISDA 2018 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (e): Conditions Precedent. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (f): Conditions Precedent. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (e): Conditions Precedent. | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (e): Conditions Precedent and Secured Party’s Rights and Remedies.
  """
  accessConditions: AccessConditions = Field(..., description="The parties' election with respect to the Termination Events that will be deemed an Access Condition (Initial Margin CSA) or a Specified Condition (Variation Margin CSA). ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (e)(ii). | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (f)(ii). | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (e)(ii). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (e): Conditions Precedent and Secured Party’s Rights and Remedies.")
  """
  The parties' election with respect to the Termination Events that will be deemed an Access Condition (Initial Margin CSA) or a Specified Condition (Variation Margin CSA). ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (e)(ii). | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (f)(ii). | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (e)(ii). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (e): Conditions Precedent and Secured Party’s Rights and Remedies.
  """
  conditionsPrecedentElection: Optional[ExceptionEnum] = Field(None, description="The election to specify whether the standard Conditions Precedent apply")
  """
  The election to specify whether the standard Conditions Precedent apply
  """
  customProvision: Optional[str] = Field(None, description="The custom provisions that might be specified by the parties to the agreement for the purpose of overwriting the default Condition Precedent provision as specified in ISDA 2016 Credit Support Annex for Initial Margin and the ISDA 2016 Credit Support Annex for Variation Margin, Paragraph 4, (a). ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (e)(i). | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (f)(i). | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (e)(i). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, : Conditions Precedent and Secured Party’s Rights and Remedies.")
  """
  The custom provisions that might be specified by the parties to the agreement for the purpose of overwriting the default Condition Precedent provision as specified in ISDA 2016 Credit Support Annex for Initial Margin and the ISDA 2016 Credit Support Annex for Variation Margin, Paragraph 4, (a). ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (e)(i). | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (f)(i). | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (e)(i). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, : Conditions Precedent and Secured Party’s Rights and Remedies.
  """
  
  @rosetta_condition
  def condition_0_CustomProvision(self):
    """
    When a Custom Provision is specified then the Conditions Precedent Election should be absent.
    """
    def _then_fn0():
      return all_elements(self.conditionsPrecedentElection, "=", ExceptionEnum.OTHER)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.customProvision) is not None), _then_fn0, _else_fn0)

from cdm.legaldocumentation.csa.AccessConditions import AccessConditions
from cdm.legaldocumentation.csa.ExceptionEnum import ExceptionEnum

ConditionsPrecedent.update_forward_refs()
