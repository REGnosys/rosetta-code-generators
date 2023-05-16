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

__all__ = ['RetrospectiveEffect']


class RetrospectiveEffect(BaseDataClass):
  """
  A class to specify the retrospective effect exception to the regulatory regime clause of Initial Margin documents as either a normalized value specified as part of an enumeration or a customized value specified of type string.
  """
  asSpecified: Optional[str] = Field(None, description="The Standard Initial Margin Model exception when specified as a customized approach by the party.")
  """
  The Standard Initial Margin Model exception when specified as a customized approach by the party.
  """
  standardisedException: Optional[ExceptionEnum] = Field(None, description="The Standard Initial Margin Model exception when specified by the party according to one of the enumerated values.")
  """
  The Standard Initial Margin Model exception when specified by the party according to one of the enumerated values.
  """

from cdm.legaldocumentation.csa.ExceptionEnum import ExceptionEnum

RetrospectiveEffect.update_forward_refs()
