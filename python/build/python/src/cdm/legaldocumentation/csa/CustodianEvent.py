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

__all__ = ['CustodianEvent']


class CustodianEvent(BaseDataClass):
  """
  A class to specify the Custodian Event (English Law & New York Law ISDA CSA) and the Collateral Manager Event (Japanese Law ISDA CSA) in terms of applicability and end-date. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (n)(iii): Custodian Event. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (m)(ii): Collateral Manager Event. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(iii): Custodian Event.
  """
  endDate: Optional[CustodianEventEndDate] = Field(None, description="The qualification of the Custodian Event (English Law & New York Law ISDA CSA) or Collateral Manager Event (Japanese Law ISDA CSA) End Date.")
  """
  The qualification of the Custodian Event (English Law & New York Law ISDA CSA) or Collateral Manager Event (Japanese Law ISDA CSA) End Date.
  """
  isApplicable: bool = Field(..., description="The qualification as to whether the Custodian Event (English Law & New York Law ISDA CSA) or the Collateral Manager Event (Japanese Law ISDA CSA) is applicable.")
  """
  The qualification as to whether the Custodian Event (English Law & New York Law ISDA CSA) or the Collateral Manager Event (Japanese Law ISDA CSA) is applicable.
  """

from cdm.legaldocumentation.csa.CustodianEventEndDate import CustodianEventEndDate

CustodianEvent.update_forward_refs()
