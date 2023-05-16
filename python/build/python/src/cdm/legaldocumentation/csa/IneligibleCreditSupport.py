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

__all__ = ['IneligibleCreditSupport']


class IneligibleCreditSupport(BaseDataClass):
  """
  A class to specify the parties to which the provisions of Paragraph 11(g) of the ISDA 2016 Credit Support Annex for Variation Margin will apply to. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (c)(iii): Legally Ineligible Credit Support (VM).
  """
  specifiedParty: List[AttributeWithReference | Party] = Field([], description="The parties to which the provisions of Paragraph 11(g) of the ISDA 2016 Credit Support Annex for Variation Margin will apply to, as the Secured Party. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (c)(iii): Legally Ineligible Credit Support (VM).")
  """
  The parties to which the provisions of Paragraph 11(g) of the ISDA 2016 Credit Support Annex for Variation Margin will apply to, as the Secured Party. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (c)(iii): Legally Ineligible Credit Support (VM).
  """
  @rosetta_condition
  def cardinality_specifiedParty(self):
    return check_cardinality(self.specifiedParty, 0, 2)
  
  totalIneligibilityDate: Optional[str] = Field(None, description="Total Ineligibility Date has the meaning specified in Paragraph 11(g), unless otherwise specified here.")
  """
  Total Ineligibility Date has the meaning specified in Paragraph 11(g), unless otherwise specified here.
  """
  transferIneligibilityDate: Optional[str] = Field(None, description="Transfer Ineligibility Date has the meaning specified in Paragraph 11(g), unless otherwise specified here.")
  """
  Transfer Ineligibility Date has the meaning specified in Paragraph 11(g), unless otherwise specified here.
  """

from cdm.base.staticdata.party.Party import Party

IneligibleCreditSupport.update_forward_refs()
