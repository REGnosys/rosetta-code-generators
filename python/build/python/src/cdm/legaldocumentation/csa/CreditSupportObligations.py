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

__all__ = ['CreditSupportObligations']


class CreditSupportObligations(BaseDataClass):
  """
  A class to specify the Credit Support Obligations applicable to the Initial Margin Credit Support Annex and which are common among the English, Japanese and New York governing laws. This excludes the Other Eligible Support election (which only applies to the Japanese Law and New York Law agreements) and the Transfer Timing election (which only applies to the English Law and the New York Law agreements). ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (c): Credit Support Obligations. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d): Credit Support Obligations. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (c): Credit Support Obligations.
  """
  bespokeTransferTiming: Optional[BespokeTransferTiming] = Field(None, description="The time by which the transfer of collateral must take place when different from the Regular Settlement Day as a result of parties' election.")
  """
  The time by which the transfer of collateral must take place when different from the Regular Settlement Day as a result of parties' election.
  """
  creditSupportObligationsVariationMargin: Optional[CreditSupportObligationsVariationMargin] = Field(None, description="The specification of Credit Support Obligations applicable to Variation Margin agreements.")
  """
  The specification of Credit Support Obligations applicable to Variation Margin agreements.
  """
  deliveryAmount: Optional[str] = Field(None, description="Delivery Amount (VM) has the meaning specified in Paragraph 3(a), unless otherwise specified here.")
  """
  Delivery Amount (VM) has the meaning specified in Paragraph 3(a), unless otherwise specified here.
  """
  marginApproach: Optional[MarginApproach] = Field(None, description="The selection of Margin Approach applicable to the agreement.")
  """
  The selection of Margin Approach applicable to the agreement.
  """
  minimumTransferAmount: MinimumTransferAmount = Field(..., description="The net amount of exposure reached before collateral has to be posted or returned. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (c)(vi)(B): Minimum Transfer Amount. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(vi)(B): Minimum Transfer Amount. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (c)(vi)(B): Minimum Transfer Amount.")
  """
  The net amount of exposure reached before collateral has to be posted or returned. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (c)(vi)(B): Minimum Transfer Amount. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(vi)(B): Minimum Transfer Amount. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (c)(vi)(B): Minimum Transfer Amount.
  """
  otherEligibleSupport: Optional[str] = Field(None, description="The Other Eligible Support election. If not specified, this election is deemed as not applicable.")
  """
  The Other Eligible Support election. If not specified, this election is deemed as not applicable.
  """
  returnAmount: Optional[str] = Field(None, description="Return Amount (VM) has the meaning specified in Paragraph 3(a), unless otherwise specified here.")
  """
  Return Amount (VM) has the meaning specified in Paragraph 3(a), unless otherwise specified here.
  """
  rounding: Optional[CollateralRounding] = Field(None, description="The rounding methodology applicable to the Delivery Amount and the Return Amount in terms of nearest integral multiple of Base Currency units. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (c)(vi)(C): Rounding. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(vi)(C): Rounding. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (c)(vi)(C): Rounding.")
  """
  The rounding methodology applicable to the Delivery Amount and the Return Amount in terms of nearest integral multiple of Base Currency units. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (c)(vi)(C): Rounding. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(vi)(C): Rounding. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (c)(vi)(C): Rounding.
  """
  threshold: Threshold = Field(..., description="The amount of net exposure that a party is willing to bear in relation to the other party before it requires asking for collateral. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (c)(vi)(A): Threshold. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(vi)(A): Threshold. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (c)(vi)(A): Threshold.")
  """
  The amount of net exposure that a party is willing to bear in relation to the other party before it requires asking for collateral. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (c)(vi)(A): Threshold. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(vi)(A): Threshold. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (c)(vi)(A): Threshold.
  """

from cdm.legaldocumentation.csa.BespokeTransferTiming import BespokeTransferTiming
from cdm.legaldocumentation.csa.CreditSupportObligationsVariationMargin import CreditSupportObligationsVariationMargin
from cdm.legaldocumentation.csa.MarginApproach import MarginApproach
from cdm.legaldocumentation.csa.MinimumTransferAmount import MinimumTransferAmount
from cdm.legaldocumentation.csa.CollateralRounding import CollateralRounding
from cdm.legaldocumentation.csa.Threshold import Threshold

CreditSupportObligations.update_forward_refs()
