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

__all__ = ['SubstitutedRegimeTerms']


class SubstitutedRegimeTerms(BaseDataClass):
  """
  Specifies the applicability of the Substituted Regime as denoted in the Substituted Regime Table as part of certain legal agreements, such as such as the ISDA 2016 and 2018 CSA for Initial Margin.
  """
  isApplicable: bool = Field(..., description="The specification of whether the regime is elected as applicable to the party when acting as collateral taker.")
  """
  The specification of whether the regime is elected as applicable to the party when acting as collateral taker.
  """
  party: CounterpartyRoleEnum = Field(..., description="The party for which the regime terms are being specified when acting as collateral taker.")
  """
  The party for which the regime terms are being specified when acting as collateral taker.
  """

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

SubstitutedRegimeTerms.update_forward_refs()
