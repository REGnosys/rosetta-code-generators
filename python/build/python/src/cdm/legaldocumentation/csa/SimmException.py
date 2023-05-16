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

__all__ = ['SimmException']


class SimmException(BaseDataClass):
  """
  A class to specify the SIMM exception to the regulatory regime clause of the ISDA 2016 and 2018 CSA for Initial Margin as either a normalized value specified as part of an enumeration or a customized value specified of type string. ISDA 2016 Credit Support Annex for Initial Margin paragraph 13, Regime: SIMM Exception.
  """
  asSpecified: Optional[str] = Field(None, description="The Standard Initial Margin Model exception when specified as a customized approach by the party.")
  """
  The Standard Initial Margin Model exception when specified as a customized approach by the party.
  """
  simmExceptionApplicable: Optional[SimmExceptionApplicableEnum] = Field(None, description="The Standard Initial Margin model exception approach applicable when specified by the party according to one of the enumerated values.")
  """
  The Standard Initial Margin model exception approach applicable when specified by the party according to one of the enumerated values.
  """
  standardisedException: Optional[ExceptionEnum] = Field(None, description="The Standard Initial Margin Model exception when specified by the party according to one of the enumerated values.")
  """
  The Standard Initial Margin Model exception when specified by the party according to one of the enumerated values.
  """

from cdm.legaldocumentation.csa.SimmExceptionApplicableEnum import SimmExceptionApplicableEnum
from cdm.legaldocumentation.csa.ExceptionEnum import ExceptionEnum

SimmException.update_forward_refs()
