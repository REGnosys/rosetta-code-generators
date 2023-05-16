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

__all__ = ['CustodyArrangements']


class CustodyArrangements(BaseDataClass):
  """
  A class to specify the Custody Arrangements for the agreement.
  """
  collateralAccessBreach: Optional[CollateralAccessBreach] = Field(None, description="The elections specific to Collateral Access Breach language")
  """
  The elections specific to Collateral Access Breach language
  """
  collateralManagementAgreement: Optional[CollateralManagementAgreement] = Field(None, description="ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (b)(i): Collateral Management Agreement.")
  """
  ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (b)(i): Collateral Management Agreement.
  """
  controlAgreement: Optional[ControlAgreement] = Field(None, description="The party-specific election with respect to the control agreement.")
  """
  The party-specific election with respect to the control agreement.
  """
  custodian: Optional[Custodian] = Field(None, description="The custodian and segregated account details for each party to the agreement.")
  """
  The custodian and segregated account details for each party to the agreement.
  """
  custodianEvent: CustodianEvent = Field(..., description="When specified as True, means that the Custodian Events specified in Paragraph 13 General Principles, (m)(iii) will constitute an Additional Termination Event. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (m)(iii): Custodian Event.")
  """
  When specified as True, means that the Custodian Events specified in Paragraph 13 General Principles, (m)(iii) will constitute an Additional Termination Event. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (m)(iii): Custodian Event.
  """
  custodianRisk: Optional[CustodianRisk] = Field(None, description="The qualification of the Custodian Risk. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii): Custodian (IM) Risk.")
  """
  The qualification of the Custodian Risk. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii): Custodian (IM) Risk.
  """
  hasControlAgreementLanguage: Optional[bool] = Field(None, description="Control Agreement language is specified when True.")
  """
  Control Agreement language is specified when True.
  """
  isCreditSupportDocument: Optional[bool] = Field(None, description="Unless specified as True, the Control Agreement is not a Credit Support Document under the agreement with respect to a party. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 6 (e): The Control Agreement as a Credit Support Document.")
  """
  Unless specified as True, the Control Agreement is not a Credit Support Document under the agreement with respect to a party. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 6 (e): The Control Agreement as a Credit Support Document.
  """
  otherProvisions: Optional[str] = Field(None, description="ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(vii): Other Provisions.")
  """
  ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(vii): Other Provisions.
  """

from cdm.legaldocumentation.csa.CollateralAccessBreach import CollateralAccessBreach
from cdm.legaldocumentation.csa.CollateralManagementAgreement import CollateralManagementAgreement
from cdm.legaldocumentation.csa.ControlAgreement import ControlAgreement
from cdm.legaldocumentation.csa.Custodian import Custodian
from cdm.legaldocumentation.csa.CustodianEvent import CustodianEvent
from cdm.legaldocumentation.csa.CustodianRisk import CustodianRisk

CustodyArrangements.update_forward_refs()
