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

__all__ = ['Observation']


class Observation(BaseDataClass):
  """
  Defines a single, numerical value that was observed in the marketplace. Observations of market data are made independently to business events or trade life-cycle events, so data instances of Observation can be created independently of any other model type, hence it is annotated as a root type. Observations will be broadly reused in many situations, so references to Observation are supported via the 'key' annotation.
  """
  observationIdentifier: ObservationIdentifier = Field(..., description="Represents the observation was made i.e. how to uniquely identify the observed value among the population of all available market data.")
  """
  Represents the observation was made i.e. how to uniquely identify the observed value among the population of all available market data.
  """
  observedValue: Price = Field(..., description="Specifies the observed value as a number.")
  """
  Specifies the observed value as a number.
  """

from cdm.observable.event.ObservationIdentifier import ObservationIdentifier
from cdm.observable.asset.Price import Price

Observation.update_forward_refs()
