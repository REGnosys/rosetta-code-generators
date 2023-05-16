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

__all__ = ['RightsEvents']


class RightsEvents(BaseDataClass):
  """
  A class to specify the rights of Security Taker and/or Security Provider when an Early Termination or Access Condition event has occurred.
  """
  additionalRightsEvent: Optional[AdditionalRightsEvent] = Field(None, description="The Additional Rights Event election.")
  """
  The Additional Rights Event election.
  """
  controlAgreementNecEvent: Optional[ControlAgreementNecEvent] = Field(None, description="The bespoke provisions that might be specified by the parties to the agreement applicable to a Notice of Exclusive Control Event.")
  """
  The bespoke provisions that might be specified by the parties to the agreement applicable to a Notice of Exclusive Control Event.
  """
  deliveryInLieuRight: Optional[bool] = Field(None, description="The specification of whether Delivery In Lieu language is applicable to the agreement (true) or not (false).")
  """
  The specification of whether Delivery In Lieu language is applicable to the agreement (true) or not (false).
  """
  securityProviderRightsEvent: SecurityProviderRightsEvent = Field(..., description="The bespoke provisions that might be specified by the parties to the agreement applicable to a Security Provider Rights Event.")
  """
  The bespoke provisions that might be specified by the parties to the agreement applicable to a Security Provider Rights Event.
  """
  securityTakerRightsEvent: SecuredPartyRightsEvent = Field(..., description="The bespoke provisions that might be specified by the parties to the agreement applicable to a Security Taker Rights Event.")
  """
  The bespoke provisions that might be specified by the parties to the agreement applicable to a Security Taker Rights Event.
  """

from cdm.legaldocumentation.csa.AdditionalRightsEvent import AdditionalRightsEvent
from cdm.legaldocumentation.csa.ControlAgreementNecEvent import ControlAgreementNecEvent
from cdm.legaldocumentation.csa.SecurityProviderRightsEvent import SecurityProviderRightsEvent
from cdm.legaldocumentation.csa.SecuredPartyRightsEvent import SecuredPartyRightsEvent

RightsEvents.update_forward_refs()
