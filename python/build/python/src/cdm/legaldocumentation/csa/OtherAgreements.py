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

__all__ = ['OtherAgreements']


class OtherAgreements(BaseDataClass):
  """
  The bespoke definition of other agreement terms as specified by the parties to the agreement.
  """
  japaneseLawCsa: Optional[OtherAgreementTerms] = Field(None, description="The bespoke definition of whether Japanese Law CSA (VM) are specified by the parties to the agreement. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (s)(ii): Japanese Law CSA (VM).")
  """
  The bespoke definition of whether Japanese Law CSA (VM) are specified by the parties to the agreement. ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (s)(ii): Japanese Law CSA (VM).
  """
  otherCsa: Optional[OtherAgreementTerms] = Field(None, description="The bespoke definition of Other CSA as specified by the parties to the agreement.")
  """
  The bespoke definition of Other CSA as specified by the parties to the agreement.
  """

from cdm.legaldocumentation.common.OtherAgreementTerms import OtherAgreementTerms

OtherAgreements.update_forward_refs()
