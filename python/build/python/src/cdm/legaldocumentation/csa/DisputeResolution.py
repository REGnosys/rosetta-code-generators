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

__all__ = ['DisputeResolution']


class DisputeResolution(BaseDataClass):
  """
  A class to specify the election terms under which a party disputes (i) the Calculation Agent’s calculation of a Delivery Amount or a Return Amount, or (ii) the Value of any Transfer of Eligible Credit Support or Posted Credit Support. Parties can specify such election either through a business center time or through a custom election. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (g): Dispute Resolution. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (h): Dispute Resolution. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (g): Dispute Resolution.
  """
  alternativeTerms: Optional[str] = Field(None, description="The alternative dispute resolution procedure if specified")
  """
  The alternative dispute resolution procedure if specified
  """
  otherTerms: Optional[str] = Field(None, description="The custom Resolution Time election that might be specified by the parties.")
  """
  The custom Resolution Time election that might be specified by the parties.
  """
  recalculationOfValue: Optional[RecalculationOfValue] = Field(None, description="The elections to specify terms for recalculation of the market value of posted collateral.")
  """
  The elections to specify terms for recalculation of the market value of posted collateral.
  """
  resolutionTime: Optional[BusinessCenterTime] = Field(None, description="The time by which the dispute needs to be resolved, failure of which would trigger a recalculation alongside a process that is specified as part of the agreement. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (g)(i): Resolution Time. | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (g)(i): Resolution Time.")
  """
  The time by which the dispute needs to be resolved, failure of which would trigger a recalculation alongside a process that is specified as part of the agreement. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (g)(i): Resolution Time. | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (g)(i): Resolution Time.
  """
  valueTerms: str = Field(..., description="The method of calculation for determining value for the purposes of a Variation Margin agreement.")
  """
  The method of calculation for determining value for the purposes of a Variation Margin agreement.
  """

from cdm.legaldocumentation.csa.RecalculationOfValue import RecalculationOfValue
from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime

DisputeResolution.update_forward_refs()
