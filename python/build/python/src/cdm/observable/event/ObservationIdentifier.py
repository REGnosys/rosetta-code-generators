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

__all__ = ['ObservationIdentifier']


class ObservationIdentifier(BaseDataClass):
  """
  Defines the parameters needed to uniquely identify a piece of data among the population of all available market data.
  """
  determinationMethodology: Optional[DeterminationMethodology] = Field(None, description="Specifies the method according to which an amount or a date is determined.")
  """
  Specifies the method according to which an amount or a date is determined.
  """
  informationSource: Optional[InformationSource] = Field(None, description="Represents where the market data published and should be observed.")
  """
  Represents where the market data published and should be observed.
  """
  observable: Observable = Field(..., description="Represents the asset or rate to which the observation relates.")
  """
  Represents the asset or rate to which the observation relates.
  """
  observationDate: date = Field(..., description="Specifies the date value to use when resolving the market data.")
  """
  Specifies the date value to use when resolving the market data.
  """
  observationTime: Optional[TimeZone] = Field(None, description="Represents the time and time-zone.")
  """
  Represents the time and time-zone.
  """

from cdm.observable.event.DeterminationMethodology import DeterminationMethodology
from cdm.observable.asset.InformationSource import InformationSource
from cdm.observable.asset.Observable import Observable
from cdm.base.datetime.TimeZone import TimeZone

ObservationIdentifier.update_forward_refs()
