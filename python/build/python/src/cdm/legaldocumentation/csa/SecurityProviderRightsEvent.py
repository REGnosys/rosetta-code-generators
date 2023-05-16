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

__all__ = ['SecurityProviderRightsEvent']


class SecurityProviderRightsEvent(BaseDataClass):
  """
  A class to specify the Pledgor/Obligor/Chargor Rights Event election. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (j): Chargor Rights Event. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (j): Obligor Rights Event. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (j): Pledgor Rights Event.
  """
  automaticSetOff: Optional[bool] = Field(None, description="The Automatic Set-Off provision applies when the value is set to True. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (l): Modification to Obligor’s Rights and Remedies.")
  """
  The Automatic Set-Off provision applies when the value is set to True. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (l): Modification to Obligor’s Rights and Remedies.
  """
  customElection: Optional[str] = Field(None, description="A custom Pledgor/Obligor/Chargor Rights Event election might be specified by the parties.")
  """
  A custom Pledgor/Obligor/Chargor Rights Event election might be specified by the parties.
  """
  fullDischarge: Optional[bool] = Field(None, description="If specified as applicable here, a Pledgor/Obligor/Chargor Rights Event will not occur unless the Pledgor/Obligor/Chargor (A) has provided a statement to the Secured Party in respect of such Early                       Termination Date")
  """
  If specified as applicable here, a Pledgor/Obligor/Chargor Rights Event will not occur unless the Pledgor/Obligor/Chargor (A) has provided a statement to the Secured Party in respect of such Early                       Termination Date
  """
  includeCoolingOffLanguage: bool = Field(..., description="The Pledgor/Obligor/Chargor Rights Event election includes cooling off language when the attribute is set of True.")
  """
  The Pledgor/Obligor/Chargor Rights Event election includes cooling off language when the attribute is set of True.
  """
  partyElection: List[SecurityProviderRightsEventElection] = Field([], description="")
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 0, 2)
  
  
  @rosetta_condition
  def condition_0_RightsEvent_includeCoolingOffLanguage(self):
    """
    A data rule to enforce that, when the Rights Event election includes cooling off language, no custom election should be specified.
    """
    def _then_fn0():
      return ((self.customElection) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.includeCoolingOffLanguage, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_RightsEvent_customElection(self):
    """
    A data rule to enforce that, when the Rights Event is specified through a custom election, no standard cooling off language should be specified.
    """
    def _then_fn0():
      return all_elements(self.includeCoolingOffLanguage, "=", False)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.customElection) is not None), _then_fn0, _else_fn0)

from cdm.legaldocumentation.csa.SecurityProviderRightsEventElection import SecurityProviderRightsEventElection

SecurityProviderRightsEvent.update_forward_refs()
