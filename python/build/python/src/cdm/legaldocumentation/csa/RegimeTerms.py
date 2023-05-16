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

__all__ = ['RegimeTerms']


class RegimeTerms(BaseDataClass):
  """
  A class that is used by the ApplicableRegime and the AdditionalRegime classes to specify the regulatory regime terms which are referred to as part of certain legal agreements, such as such as the ISDA 2016 and 2018 CSA for Initial Margin.
  """
  asSpecified: Optional[str] = Field(None, description="The bespoke party specific Regime term elections applicable when specified.")
  """
  The bespoke party specific Regime term elections applicable when specified.
  """
  isApplicable: Optional[ExceptionEnum] = Field(None, description="The specification of whether the regime is elected as applicable to the party when acting as collateral taker.")
  """
  The specification of whether the regime is elected as applicable to the party when acting as collateral taker.
  """
  party: CounterpartyRoleEnum = Field(..., description="The party for which the regime terms are being specified when acting as collateral taker.")
  """
  The party for which the regime terms are being specified when acting as collateral taker.
  """
  retrospectiveEffect: Optional[RetrospectiveEffect] = Field(None, description="ISDA 2016 CSA for Initial Margin, paragraph 13 (b)(i): if `Retrospective Effect` is specified as applicable to a Regime (a `Retrospective Regime`) then all Covered Transactions (IM) under all other Regimes with an earlier Regime Effective Time will, to the extent that they would have been Covered Transactions (IM) under such Retrospective Regime had such Transactions been entered into at or after the Regime Effective Time of the Retrospective Regime, be deemed to be Covered Transactions (IM) for such Retrospective Regime.")
  """
  ISDA 2016 CSA for Initial Margin, paragraph 13 (b)(i): if `Retrospective Effect` is specified as applicable to a Regime (a `Retrospective Regime`) then all Covered Transactions (IM) under all other Regimes with an earlier Regime Effective Time will, to the extent that they would have been Covered Transactions (IM) under such Retrospective Regime had such Transactions been entered into at or after the Regime Effective Time of the Retrospective Regime, be deemed to be Covered Transactions (IM) for such Retrospective Regime.
  """
  simmException: Optional[SimmException] = Field(None, description="The election for SIMM exception to the regulatory regime clause of the ISDA 2016 and 2018 CSA for Initial Margin as either a normalized value specified as part of an enumeration or a customized value specified of type string. ISDA 2016 Credit Support Annex for Initial Margin paragraph 13, Regime: SIMM Exception.")
  """
  The election for SIMM exception to the regulatory regime clause of the ISDA 2016 and 2018 CSA for Initial Margin as either a normalized value specified as part of an enumeration or a customized value specified of type string. ISDA 2016 Credit Support Annex for Initial Margin paragraph 13, Regime: SIMM Exception.
  """

from cdm.legaldocumentation.csa.ExceptionEnum import ExceptionEnum
from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum
from cdm.legaldocumentation.csa.RetrospectiveEffect import RetrospectiveEffect
from cdm.legaldocumentation.csa.SimmException import SimmException

RegimeTerms.update_forward_refs()
