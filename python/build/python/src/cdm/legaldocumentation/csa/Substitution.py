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

__all__ = ['Substitution']


class Substitution(BaseDataClass):
  """
  A class to specify the conditions under which the Security Provider can substitute posted collateral.
  """
  needsConsent: bool = Field(..., description="The election as to whether the Pledgor/Obligor/Chargor must obtain the Secured Party’s consent for any collateral substitution. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (f)(ii): Consent. | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (f)(ii): Consent.")
  """
  The election as to whether the Pledgor/Obligor/Chargor must obtain the Secured Party’s consent for any collateral substitution. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (f)(ii): Consent. | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (f)(ii): Consent.
  """
  specificConsentLanguage: Optional[str] = Field(None, description="Specific consent language might be specified by the parties.")
  """
  Specific consent language might be specified by the parties.
  """
  substitutionDateLanguage: Optional[str] = Field(None, description="Substiution   Date  has  the  meaning  specified  in  Paragraph4(d)(ii),   unless   otherwise   specified.")
  """
  Substiution   Date  has  the  meaning  specified  in  Paragraph4(d)(ii),   unless   otherwise   specified.
  """


Substitution.update_forward_refs()
