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

__all__ = ['CustodianEventEndDate']


class CustodianEventEndDate(BaseDataClass):
  """
  A class to specify the Custodian Event (English Law & New York Law ISDA CSA) or Collateral Manager Event (Japanese Law ISDA CSA) End Date. Its qualification is function of three elective periods: either (i) a specified number of days after the occurrence of the Custodian Event (the daysAfterCustodianEvent attribute), or (ii) the number of days prior to the date on which the Control Agreement will terminate, with in this latter case (iii) the further qualification of the number of days prior to the Release Date if only one party has effectively provided the Timely Statement to the other party. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (n)(iii): CE End Date. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (m)(ii): CME End Date. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(iii): CE End Date.
  """
  dateOfTimelyStatement: CustomisableOffset = Field(..., description="The parties' election to specify the number of days one party has effectively provided the Timely Statement to the other party.")
  """
  The parties' election to specify the number of days one party has effectively provided the Timely Statement to the other party.
  """
  daysAfterCustodianEvent: CustomisableOffset = Field(..., description="The parties' election to specify the number of days after the occurrence of the Custodian Event (English Law & New York Law ISDA CSA) or the Collateral Management Event (Japanese Law ISDA CSA) for the purpose of qualifying the CE/CME End Date.")
  """
  The parties' election to specify the number of days after the occurrence of the Custodian Event (English Law & New York Law ISDA CSA) or the Collateral Management Event (Japanese Law ISDA CSA) for the purpose of qualifying the CE/CME End Date.
  """
  releaseDate: CustomisableOffset = Field(..., description="The parties' election to specify the number of days prior to the termination of the Control Agreement (English Law & New York Law ISDA CSA) or the Collateral Management Event (Japanese Law ISDA CSA) for the purpose of qualifying the CE/CME End Date, in the case where advance notice is given.")
  """
  The parties' election to specify the number of days prior to the termination of the Control Agreement (English Law & New York Law ISDA CSA) or the Collateral Management Event (Japanese Law ISDA CSA) for the purpose of qualifying the CE/CME End Date, in the case where advance notice is given.
  """
  safekeepingPeriodExpiry: Optional[CustomisableOffset] = Field(None, description="The parties' election to specify the number of days prior to the end of the safekeeping period (Clearstream CTA) purpose of qualifying the CE/CME End Date, in the case where advance notice is given.")
  """
  The parties' election to specify the number of days prior to the end of the safekeeping period (Clearstream CTA) purpose of qualifying the CE/CME End Date, in the case where advance notice is given.
  """

from cdm.base.datetime.CustomisableOffset import CustomisableOffset

CustodianEventEndDate.update_forward_refs()
