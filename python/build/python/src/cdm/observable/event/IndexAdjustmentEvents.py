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

__all__ = ['IndexAdjustmentEvents']


class IndexAdjustmentEvents(BaseDataClass):
  """
  Defines the specification of the consequences of Index Events as defined by the 2002 ISDA Equity Derivatives Definitions.
  """
  indexCancellation: IndexEventConsequenceEnum = Field(..., description="Consequence of index cancellation.")
  """
  Consequence of index cancellation.
  """
  indexDisruption: IndexEventConsequenceEnum = Field(..., description="Consequence of index disruption.")
  """
  Consequence of index disruption.
  """
  indexModification: IndexEventConsequenceEnum = Field(..., description="Consequence of index modification.")
  """
  Consequence of index modification.
  """

from cdm.observable.event.IndexEventConsequenceEnum import IndexEventConsequenceEnum

IndexAdjustmentEvents.update_forward_refs()
