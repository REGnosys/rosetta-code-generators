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

__all__ = ['CalculationAndTiming']


class CalculationAndTiming(BaseDataClass):
  """
  A class to specify the Calculation, Valuation and Timing terms specific to the agreement.
  """
  bespokeCalculationDate: Optional[BespokeCalculationDate] = Field(None, description="The specification of bespoke Calculation Date terms for the purposes of Initial or Variation Margin by the parties to the agreement.")
  """
  The specification of bespoke Calculation Date terms for the purposes of Initial or Variation Margin by the parties to the agreement.
  """
  bespokeCalculationTime: Optional[BespokeCalculationTime] = Field(None, description="Bespoke terms to describe the time as of which such party (or the Calculation Agent (IM) (if applicale)) computes its end of day valuations of derivatives transactions.")
  """
  Bespoke terms to describe the time as of which such party (or the Calculation Agent (IM) (if applicale)) computes its end of day valuations of derivatives transactions.
  """
  calculationAgentTerms: Optional[CalculationAgentTerms] = Field(None, description="The calculation agent terms applicable to the agreement.")
  """
  The calculation agent terms applicable to the agreement.
  """
  calculationDateLocation: Optional[CalculationDateLocation] = Field(None, description="The specified location where the credit exposure will be calculated by the respective parties.")
  """
  The specified location where the credit exposure will be calculated by the respective parties.
  """
  cashSettlementDay: Optional[str] = Field(None, description="Cash Settlement Day has the meaning specified in ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, Paragraph 4(b)(i), unless otherwise specified as part of this attribute.")
  """
  Cash Settlement Day has the meaning specified in ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, Paragraph 4(b)(i), unless otherwise specified as part of this attribute.
  """
  collateralValuationAgent: Optional[CollateralValuationAgent] = Field(None, description="The bespoke Collateral Valuation Agent terms applicable to the agreement.")
  """
  The bespoke Collateral Valuation Agent terms applicable to the agreement.
  """
  notificationTime: NotificationTime = Field(..., description="The time by which a demand for the Transfer of Eligible Credit Support (IM) or Posted Credit Support (IM) needs to be made in order for the transfer to take place in accordance with the Transfer Timing provisions.")
  """
  The time by which a demand for the Transfer of Eligible Credit Support (IM) or Posted Credit Support (IM) needs to be made in order for the transfer to take place in accordance with the Transfer Timing provisions.
  """
  securitiesSettlementDay: Optional[str] = Field(None, description="Securities Settlement Day has the meaning specified in ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, Paragraph 12, unless otherwise specified as part of this attribute.")
  """
  Securities Settlement Day has the meaning specified in ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, Paragraph 12, unless otherwise specified as part of this attribute.
  """

from cdm.legaldocumentation.csa.BespokeCalculationDate import BespokeCalculationDate
from cdm.legaldocumentation.csa.BespokeCalculationTime import BespokeCalculationTime
from cdm.legaldocumentation.csa.CalculationAgentTerms import CalculationAgentTerms
from cdm.legaldocumentation.csa.CalculationDateLocation import CalculationDateLocation
from cdm.legaldocumentation.csa.CollateralValuationAgent import CollateralValuationAgent
from cdm.legaldocumentation.csa.NotificationTime import NotificationTime

CalculationAndTiming.update_forward_refs()
